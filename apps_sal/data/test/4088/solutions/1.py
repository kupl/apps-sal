from math import *

def r1(t):
    return t(input())

def r2(t):
    return [t(i) for i in input().split()]

def r3(t):
    return [t(i) for i in input()]

for _ in range(r1(int)):
    s = r3(str)
    m = r1(int)
    b = r2(int)

    s.sort()
    mp = {}
    for i in s:
        mp[i] = 0
    for i in s:
        mp[i] += 1
    
    t = ['' for i in range(m)]
    for i in range(m):
        ind = []
        cnt = 0
        for j in range(m):
            if b[j] == 0:
                ind.append(j)
                cnt += 1
        if (cnt == 0):
            break
        for x in ind:
            for j in range(m):
                b[j] -= max(abs(x - j), 1)

        tk = ''
        tkeys = list(sorted(list(mp.keys()), reverse=True))
        for k in tkeys:
            if mp[k] >= len(ind):
                tk = k
            del mp[k]
            if len(tk) > 0:
                break
            
        for x in ind:
            t[x] = tk
        #print(mp, b, t)

    print(''.join(t))

