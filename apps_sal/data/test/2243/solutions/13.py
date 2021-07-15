n,k,q = map(int,input().split())
t = list(map(int,input().split()))
d = {}
for i in range(n):
    d[i+1] = t[i]

sp = []

for i in range(q):
    a,b = map(int,input().split())
    if a == 1:
        if len(sp) == 0:
            sp.append(b)
        else:
            j = 0
            x = d[b]
            bb = True
            while d[sp[j]] > x:
                j += 1
                if j == len(sp):
                    if len(sp) < k:
                        sp.append(b)
                    bb = False
                    break
            if bb:
                s1 = sp[:j]
                s2 = sp[j:]
                sp = s1 + [b] + s2
                if len(sp) > k:
                    sp.remove(sp[-1])
    else:
        if b in sp:
            print('YES')
        else:
            print('NO')
