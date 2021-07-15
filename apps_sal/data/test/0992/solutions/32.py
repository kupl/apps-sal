import numpy as np

N, S = list(map(int, input().split()))
A = tuple(map(int, input().split()))
MOD = 998244353

dp = np.zeros((N + 1, S + 1), dtype=np.int64)
dp[0][0] = 1
for i in range(N):
    dp[i + 1] = dp[i] * 2
    dp[i + 1, A[i]:] += dp[i, :-A[i]]
    dp[i + 1] %= MOD

print((dp[N][S]))

