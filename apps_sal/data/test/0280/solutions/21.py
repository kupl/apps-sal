import sys
from itertools import permutations
from bisect import bisect_left


N, M = list(map(int, input().split()))
W = list(map(int, input().split()))
P = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]
INF = float('inf')

if max(W) > min(v for _, v in P):
    print((-1))
    return

P.sort(key=lambda x: (x[0], -x[1]))
cur = INF
bridge_l = []
bridge_v = []
for l, v in reversed(P):
    if v < cur:
        bridge_l.append(l)
        bridge_v.append(v)
        cur = v
bridge_l.append(0)
bridge_v.append(0)
bridge_l.reverse()
bridge_v.reverse()

ans = INF
for C in permutations(W):
    H = [0] * (N + 1)
    for i, c in enumerate(C):
        H[i] = H[i - 1] + c
    pos = [0] * N
    for i in range(1, N):
        for j in range(i):
            w = H[i] - H[j - 1]
            idx = bisect_left(bridge_v, w)
            pos[i] = max(pos[i], pos[j] + bridge_l[idx - 1])
    ans = min(ans, pos[N - 1])

print(ans)

