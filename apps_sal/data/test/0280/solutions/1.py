import sys
from operator import itemgetter
from itertools import permutations
from bisect import bisect_left


N, M = list(map(int, input().split()))
W = list(map(int, input().split()))
P = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]
if max(W) > min(P, key=itemgetter(1))[1]:
    print((-1))
    return

P.sort(key=itemgetter(1), reverse=True)
P.sort(key=itemgetter(0))

INF = float('inf')
minV = [INF] * M
for i in range(M - 1, 0, -1):
    minV[i - 1] = min(minV[i], P[i][1])

bridge_l = [0]
bridge_v = [0]
for i, (l, v) in enumerate(P):
    if v < minV[i]:
        bridge_l.append(l)
        bridge_v.append(v)

ans = INF
for C in permutations(list(range(N))):
    H = [0] * (N + 1)
    for i in range(N):
        H[i] = H[i - 1] + W[C[i]]
    pos = [0] * N
    for i in range(1, N):
        for j in range(i, -1, -1):
            w = H[i] - H[j - 1]
            idx = bisect_left(bridge_v, w)
            pos[i] = max(pos[i], bridge_l[idx - 1] + pos[j])
    ans = min(ans, pos[N - 1])

print(ans)

