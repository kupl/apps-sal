ch =input()
t=False
if ch.find('h')>=0:
    ch=ch[ch.index('h'):]
    if ch.find('e')>=0:
        ch=ch[ch.index('e'):]
        if ch.find('i')>=0:
            ch=ch[ch.index('i'):]
            if ch.find('d')>=0:
                ch=ch[ch.index('d'):]
                if ch.find('i')>=0:
                    t=True
if t:
    print('YES')
else:
    print('NO')
    

