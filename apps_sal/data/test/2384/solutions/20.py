import numpy as np
n = int(input())
a = list(map(int, input().split()))
dp = np.zeros((n + 1, 2), int)
(dp[1], dp[2]) = ([0, a[0]], [0, max(a[0], a[1])])
for i in range(3, n + 1):
    if i % 2 == 0:
        dp[i][0] = max(dp[i - 1][0], dp[i - 2][0] + a[i - 1], dp[i - 2][1])
        dp[i][1] = max(dp[i - 1][1], dp[i - 2][1] + a[i - 1])
    else:
        dp[i][0] = max(dp[i - 1][1], dp[i - 2][1], dp[i - 2][0] + a[i - 1])
        dp[i][1] = dp[i - 2][1] + a[i - 1]
print(dp[n][(n + 1) % 2])
