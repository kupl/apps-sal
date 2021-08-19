import numpy as np
(N, S) = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]
dp = np.array([0] * 3001, dtype=int)
dp[0] = 2
dp[A[0]] = 1
mod = 998244353
for a in A[1:]:
    dpn = np.zeros(3001, dtype=int)
    dpn[a:] = dp[:-a]
    dpn += dp * 2
    dpn %= mod
    dp = dpn
print(dp[S])
