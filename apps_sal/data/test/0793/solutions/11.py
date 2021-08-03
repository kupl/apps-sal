import numpy as np

N, M = list(map(int, input().split()))
S = np.array(list(map(int, input().split())))
T = np.array(list(map(int, input().split())))
MOD = 10 ** 9 + 7

neq = (S[:, None] != T[None, :])
dp = np.ones(M + 1, dtype=np.int64)
for i in range(N):
    new_dp = dp.copy()
    new_dp[1:] -= dp[:-1] * neq[i]
    np.cumsum(new_dp, out=new_dp)
    dp = new_dp % MOD
print((dp[M]))
