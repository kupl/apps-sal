import numpy as np
(N, S) = list(map(int, input().split()))
A = list(map(int, input().split()))
MOD = 998244353
ans = 0
dp = np.zeros(S + 1, dtype=np.int64)
for a in A:
    dp[0] += 1
    dp[a:] += dp[:-a].copy()
    dp %= MOD
    ans += dp[S]
print(ans % MOD)
