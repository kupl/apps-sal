import numpy as np
N, M = map(int, input().split())
S = input().split()
T = np.array(input().split(), dtype=np.int32)
dp = np.ones(M + 1, dtype=np.int64)
for s in S:
    dp[1:] = (np.where(T == int(s), dp[:-1], 0).cumsum() + dp[1:]) % (10**9 + 7)
print(dp[M])
