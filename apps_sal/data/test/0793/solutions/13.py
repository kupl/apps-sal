import numpy as np
MOD = 10 ** 9 + 7
(N, M) = map(int, input().split())
S = np.array(input().split(), dtype=np.int32)
T = np.array(input().split(), dtype=np.int32)
dp = np.ones(M + 1, dtype=np.int64)
for n in range(N):
    dp[1:] = ((dp[:-1] * (T == S[n])).cumsum() + dp[1:]) % MOD
answer = dp[M]
print(answer)
