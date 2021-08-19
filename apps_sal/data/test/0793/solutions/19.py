import numpy as np
MOD = 10 ** 9 + 7
(N, M) = list(map(int, input().split()))
s = np.array(input().split(), dtype=np.int32)
t = np.array(input().split(), dtype=np.int32)
dp = np.zeros((N + 1, M + 1), dtype=np.int64)
dp[0] = 1
for i in range(N):
    same = s[i] == t
    dp[i + 1, 1:][same] = dp[i, :-1][same]
    dp[i + 1] = (dp[i + 1].cumsum() + dp[i]) % MOD
print(dp[-1, -1])
