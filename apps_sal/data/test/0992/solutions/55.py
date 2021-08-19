import numpy as np
MOD = 998244353
(N, S) = list(map(int, input().split(' ')))
A = (0, *list(map(int, input().split(' '))))
dp = np.zeros(shape=(N + 1, S + 1), dtype=int)
dp[0][0] = 1
for i in range(1, N + 1):
    a = A[i]
    dp[i] = 2 * dp[i - 1] % MOD
    dp[i][a:] += dp[i - 1][:-a]
    dp[i] %= MOD
print(dp[N][S])
