from sys import stdin
input = stdin.readline
(v, e) = map(int, input().split())
d = {}
for i in range(1, v + 1):
    d[i] = []
for ed in range(e):
    (a, b) = map(int, input().split())
    d[a].append(b)
    d[b].append(a)
for i in d:
    d[i].sort()
sas = {}
for i in d:
    sas[tuple(d[i])] = 0
if len(sas) != 3:
    print(-1)
else:
    nbs = []
    for i in sas:
        nbs.append(set(i))
    a = nbs[0].intersection(nbs[1])
    b = nbs[0].intersection(nbs[2])
    c = nbs[1].intersection(nbs[2])
    kol = [0] * (v + 1)
    for i in a:
        kol[i] = 1
    for i in b:
        kol[i] = 2
    for i in c:
        kol[i] = 3
    zer = 0
    for i in range(1, len(kol)):
        if kol[i] == 0:
            zer += 1
            break
    if zer > 0:
        print(-1)
    elif len(a) + len(b) + len(c) != v:
        print(-1)
    else:
        print(*kol[1:])
