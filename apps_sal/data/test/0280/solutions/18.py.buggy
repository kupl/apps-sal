from bisect import bisect
from itertools import permutations
N, M = map(int, input().split())
W = list(map(int, input().split()))
LV = [tuple(map(int, input().split())) for i in range(M)]
maxw = max(W)
if any(maxw > v for l, v in LV):
    print(-1)
    return

LV.sort(key=lambda x: x[1] * 10**9 - x[0])
vl = [(0, 0)]
maxl = 0
for l, v in LV:
    if l <= maxl:
        continue
    maxl = l
    vl.append((v, l))

ans = float('inf')
for ptn in permutations(W):
    cw = [0]
    for w in ptn:
        cw.append(cw[-1] + w)
    cl = [0]
    for i in range(2, N + 1):
        nl = 0
        for j in range(i - 1):
            w = cw[i] - cw[j]
            k = bisect(vl, (w, -1))
            l = vl[k - 1][1]
            pl = cl[i - 2] - cl[j]
            nl = max(nl, l - pl)
        cl.append(cl[-1] + nl)
    ans = min(ans, cl[-1])
print(ans)
