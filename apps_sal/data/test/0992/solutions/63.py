import numpy as np

MOD = 998244353

N, S = map(int, input().split())
As = list(map(int, input().split()))

dp = np.zeros((N + 1, S + 1), np.int64)
dp[0][0] = 1
for n, A in enumerate(As):
    dp[n + 1, :] = dp[n, :] * 2
    dp[n + 1, A:] += dp[n, :-A]
    dp[n + 1] %= MOD

print(dp[N, S])
