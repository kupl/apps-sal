from itertools import permutations
from bisect import bisect_left as B
N, M = list(map(int, input().split()))
W = list(map(int, input().split()))
vls = []
for _ in range(M):
    l, v = list(map(int, input().split()))
    vls.append((v, l))
vls.sort()
rm = [0] * (M + 1)
vs = []
for i, (v, l) in enumerate(vls):
    rm[i + 1] = max(rm[i], l)
    vs.append(v)
R = 10**18
for w in permutations(W, N):
    md = [0] * N
    for i in range(N):
        hw = w[i]
        if B(vs, hw):
            R = -1
        for j in range(i + 1, N):
            hw += w[j]
            md[j] = max(md[j], md[i] + rm[B(vs, hw)])
    R = min(R, md[-1])
print(R)
