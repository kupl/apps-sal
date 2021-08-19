n = int(input())
t = [int(s) for s in input().split()]
la = set()
pl = set()
bon = True
las = 0
rep = []
for i in range(n):
    e = abs(t[i])
    if t[i] > 0:
        if e in la or e in pl:
            bon = False
            break
        else:
            la.add(e)
    elif e in la:
        la.remove(e)
        pl.add(e)
        if len(la) == 0:
            la = set()
            pl = set()
            rep.append(i + 1 - las)
            las = i + 1
    else:
        bon = False
        break
if len(la) == 0 and len(pl) == 0 and bon:
    print(len(rep))
    for i in rep:
        print(i)
else:
    print(-1)
