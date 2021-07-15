base = ord('A')

s = input()

if len(s) < 26:
    print(-1)
    return


for i in range(len(s)-25):
    ss = s[i:i+26]
    q = 0
    switch = [0] * 26
    for k in ss:
        if k == '?':
            q += 1
        else:
            switch[ord(k) - base] = 1
    if 26 - sum(switch) <= q:
        sl = list(ss)
        for ii in range(26):
            if sl[ii] == '?':
                for j in range(26):
                    if switch[j] == 0:
                        switch[j] = 1
                        sl[ii] = chr(base + j)
                        break
        news = s[0:i].replace('?','A') + ''.join(sl) + s[i+26:].replace('?','A')
        print(news)
        return
print(-1)
return
