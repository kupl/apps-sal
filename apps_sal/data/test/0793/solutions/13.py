import numpy as np
MOD = 10**9 + 7
N,M = map(int,input().split())
S = np.array(input().split(), dtype=np.int32)
T = np.array(input().split(), dtype=np.int32)

# (n,m) 以前で作れている列
dp = np.ones(M+1, dtype = np.int64)

for n in range(N):
  dp[1:] = ((dp[:-1] * (T == S[n])).cumsum() + dp[1:]) % MOD # cumsumに直す

answer = dp[M]
print(answer)
