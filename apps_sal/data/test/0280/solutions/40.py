import sys
import bisect
from itertools import permutations, accumulate
input = sys.stdin.readline
N, M = list(map(int, input().split()))
W = list(map(int, input().split()))
LV = [list(map(int, input().split())) for i in range(M)]
VL = [(v, l) for l, v in LV]
VL.sort()

V, L = list(zip(*VL))

if max(W) > min(V):
    print((-1))
    return

L = [0] + list(accumulate(L, max))

ans = 10**20

for order in permutations(list(range(N))):
    NW = [W[i] for i in order]
    t = [0, NW[0]]
    p = [0]
    for nw in NW[1:]:
        t.append(t[-1] + nw)
        ps = []
        for np, nt in zip(p, t[:-2]):
            ind = bisect.bisect_left(V, t[-1] - nt)
            ps.append(np + L[ind])
        p.append(max(ps))
    ans = min(ans, p[-1])

print(ans)
