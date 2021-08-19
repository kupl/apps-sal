import numpy as np
MOD = 10 ** 9 + 7
(N, M) = list(map(int, input().split()))
S = input().split()
T = np.array(input().split(), dtype=np.int32)
dp = np.ones(M + 1, dtype=np.int64)
for s in S:
    dp[1:] = ((dp[:-1] * (T == int(s))).cumsum() + dp[1:]) % MOD
print(dp[M])
