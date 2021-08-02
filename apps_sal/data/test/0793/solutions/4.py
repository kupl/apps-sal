import numpy as np
N, M = map(int, input().split())
MOD = 10**9 + 7
s = np.array([int(c) for c in input().split()], dtype=np.int32)
t = np.array([int(c) for c in input().split()], dtype=np.int32)
dp = np.zeros((N + 1, M + 1), np.int64)
dp[0] = 1
for i in range(N):
    mask = s[i] == t
    dp[i + 1, 1:][mask] = dp[i, :-1][mask]
    dp[i + 1] = (np.cumsum(dp[i + 1]) + dp[i]) % MOD
print(dp[-1, -1])
