import numpy as np
n, s = map(int, input().split())

a = np.array(list(map(int, input().split())))

dp = np.array([[0] * 3001 for i in range(n)])
dp[0][0] = 1
dp[0][a[0]] = 1

ans = 0
mod = 998244353
for i in range(1, n):
    dp[i] += dp[i - 1]
    dp[i][a[i]:] += dp[i - 1][:-a[i]]
    dp[i][0] += 1
    dp[i][a[i]] += 1
    dp[i] %= mod
    ans += dp[i][s]
print(ans % mod)
