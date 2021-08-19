import numpy as np
(n, s) = map(int, input().split())
a = list(map(int, input().split()))
MOD = 998244353
dp = np.zeros(s + 1, dtype=int)
dp[0] = 1
for i in range(n):
    ddp = dp * 2 % MOD
    ddp[a[i]:] += dp[:-a[i]]
    dp = ddp % MOD
print(dp[s])
