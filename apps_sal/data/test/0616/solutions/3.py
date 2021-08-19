import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9 + 7
#mod = 998244353
INF = 10**18
eps = 10**-7

N, M = list(map(int, readline().split()))
k = 2**N
dp = [INF for i in range(k)]
dp[0] = 0

for i in range(M):
    a, b = list(map(int, readline().split()))
    c = list(map(int, readline().split()))
    d = sum(1 << (ci - 1) for ci in c)
    dpnew = dp[:]
    for j in range(k):
        dpnew[j | d] = min(dp[j] + a, dpnew[j | d])
    dp = dpnew

print((dp[2**N - 1] if dp[2**N - 1] != INF else -1))
