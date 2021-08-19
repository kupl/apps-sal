from copy import deepcopy
(N, M, X) = [int(i) for i in input().split()]
CAS = [[int(i) for i in input().split()] for _ in range(N)]
ok = False
mi = [float('inf'), *[0] * M]
for i in range(2 ** N):
    t = [0] * (M + 1)
    for j in range(N):
        if i >> j & 1:
            t = [a + b for (a, b) in zip(CAS[j], t)]
    if all((a >= X for a in t[1:])) and mi[0] > t[0]:
        mi = t
        ok = True
if ok:
    print(mi[0])
else:
    print(-1)
