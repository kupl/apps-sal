import numpy as np
N, S = list(map(int, input().split()))
a = list(map(int, input().split()))

mod = 998244353


dp = np.zeros(S + 1)

dp[0] = 1

for i in range(N):
    tmp = dp * 2
    tmp[a[i]:] += dp[:-a[i]]
    dp = tmp % mod

print(int(dp[S]))
