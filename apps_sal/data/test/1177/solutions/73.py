import numpy as np
n,s = map(int,input().split())
A = list(map(int,input().split()))
mod = 998244353
ans = 0
dp = np.zeros(s+1,np.int64)
for i in A:
    dp[0] += 1
    dp[i:] += dp[:-i].copy()
    dp %= mod
    ans += dp[-1]
print(ans%mod)
