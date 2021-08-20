import numpy as np
(N, S) = map(int, input().split())
A = list(map(int, input().split()))
mod = 998244353
U = 3001
ans = 0
dp = np.zeros(U, dtype=np.int64)
dp[0] = 1
for a in A:
    newDP = np.copy(dp)
    newDP[a:] += dp[:-a]
    newDP[0] += 1
    newDP %= mod
    dp = newDP
    ans += dp[S]
    ans %= mod
print(ans)
