from itertools import accumulate
import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini] * i for _ in range(j)]


N, M, Q = mi()
LR = li2(M)

dp = dp2(0, N, N)

for l, r in LR:
    dp[l - 1][r - 1] += 1

for i in range(N):
    dp[i] = list(accumulate(dp[i]))

for i in reversed(range(N - 1)):
    for j in range(N):
        dp[i][j] += dp[i + 1][j]

for _ in range(Q):
    f, t = mi()
    print(dp[f - 1][t - 1])
