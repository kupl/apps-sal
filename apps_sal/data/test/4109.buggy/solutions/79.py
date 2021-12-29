from copy import deepcopy
(N, M, X) = [int(i) for i in input().split()]
CAS = [[int(i) for i in input().split()] for _ in range(N)]
ok = False
mi = [float('inf'), *[0] * M]
fs = '{:0' + str(N) + 'b}'
for i in range(2 ** N):
    s = fs.format(i)
    t = [0] * (M + 1)
    for (i, f) in enumerate(s):
        if f == '1':
            t = [a + b for (a, b) in zip(CAS[i], t)]
    if all((a >= X for a in t[1:])) and mi[0] > t[0]:
        mi = t
        ok = True
if ok:
    print(mi[0])
else:
    print(-1)
