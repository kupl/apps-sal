from itertools import accumulate  # list(accumulate(A))
import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini] * i for _ in range(j)]

# import bisect #bisect.bisect_left(B, a)
# from collections import defaultdict #d = defaultdict(int) d[key] += value
# from collections import Counter # a = Counter(A).most_common()


N, M, Q = mi()
LR = li2(M)

dp = dp2(0, N + 1, N + 1)

for l, r in LR:
    dp[l][r] += 1

for i in range(N + 1):
    dp[i] = list(accumulate(dp[i]))

for i in range(1, N + 1):
    for j in range(N + 1):
        dp[i][j] += dp[i - 1][j]

for _ in range(Q):
    f, t = mi()
    f_ = max(0, f - 1)
    print(dp[t][t] - dp[f_][t] - dp[t][f_] + dp[f_][f_])
