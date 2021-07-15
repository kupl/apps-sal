num = str(input())
n =len(num)
num_r = num[::-1]
s0, s5 = num_r.find('0'),num_r.find('5')
if s0 != -1:
    newnum_r = num_r[:s0] + num_r[s0+1:]
    c= []
    for a in ['0','5']:
        if newnum_r.find(a) != -1:
            c.append(newnum_r.find(a))
    if c != []:
        s = min(c)
        s0 = s0 + s
    else:
        s0 = 999999999
else:
    s0 = 999999999
if s5 != n-1 or num.find('0') != 1:
    if s5 != -1:
        newnum_r = num_r[:s5] + num_r[s5+1:]
        c= []
        for a in ['2','7']:
            if newnum_r.find(a) != -1:
                c.append(newnum_r.find(a))
        if c != []:
            s = min(c)
            s5 = s5 + s
        else:
            s5 = 999999999
    else:
        s5 = 999999999
    ssr = min(s0,s5)
    if ssr != 999999999:
        print(ssr)
    else:
        print(-1)
else:
    if s5 != -1:
        newnum_r = num_r[:s5] + num_r[s5+1:]
        c= []
        for a in ['2','7']:
            if newnum_r.find(a) != -1:
                c.append(newnum_r.find(a))
        if c != []:
            s = min(c)
            sk = 0
            for i in range(1,n-1):
                if num[i] == '0':
                    sk = sk + 1
                else:
                    break
            s5 = s5 + s + sk
        else:
            s5 = 999999999
    else:
        s5 = 999999999
    ssr = min(s0,s5)
    if ssr != 999999999:
        print(ssr)
    else:
        print(-1)
