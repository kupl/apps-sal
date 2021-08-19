import numpy as np
(N, S) = list(map(int, input().split()))
A = list(map(int, input().split()))
MOD = 998244353
dp = np.zeros(S + 1, dtype=int)
dp[0] = 1
for i in A:
    ep = dp.copy()
    ep += dp
    ep[i:] += dp[:-i]
    dp = ep % MOD
print(dp[S])
