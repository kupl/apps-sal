from bisect import bisect_left
from collections import namedtuple
from itertools import permutations

N, M = list(map(int, input().split()))
W = [int(x) for x in input().split()]
P = [tuple(map(int, input().split())) for _ in range(M)]
P.sort(key=lambda part: part[1])

ls = [p[0] for p in P]
vs = [p[1] for p in P]
for i in range(1, M):
    ls[i] = max(ls[i - 1], ls[i])

if max(W) > min(vs):
    print((-1))
    return

ans = 10 ** 20
for ws in permutations(sorted(W)):
    pref = [ws[0]]
    for i in range(1, N):
        pref.append(pref[i - 1] + ws[i])

    dp = [0] * N
    for i in range(N):
        for j in range(i):
            interval = pref[i] - (pref[j - 1] if j >= 1 else 0)
            idx = bisect_left(vs, interval)
            need = ls[idx - 1] if idx >= 1 else 0
            dp[i] = max(dp[i], dp[j] + need)

    ans = min(ans, dp[-1])

print(ans)
