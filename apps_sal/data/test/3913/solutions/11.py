n = int(input())
s = list(input())
dis = []
ind = []
ii = []
for i in range(n):
    if(s[i] != '*'):
        dis.append(s[i])
        ii.append(i)
    else:
        ind.append(i)
di = set(dis)
c = []
m = int(input())
for i in range(m):
    t = list(input())
    dp = 0
    for j in ii:
        if(t[j] != s[j]):
            dp = 1
            break
    if(dp == 0):
        q = []
        for j in ind:
            q.append(t[j])
        q = set(q)
        oo = len(q)
        q = q - di
        ooo = len(q)
        if(len(q) != 0 and oo == ooo):
            c.append(q)

if(len(c) == 0):
    print(0)
else:
    ss = c[0]
    l = len(c)
    for i in range(1, l):
        ss = ss.intersection(c[i])
    print(len(ss))
