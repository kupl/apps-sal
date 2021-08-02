import numpy as np
N = int(input())
a = []
a.append(list(map(int, input().split())))
a.append(list(map(int, input().split())))
dp = np.zeros((2, N), dtype=int)
for j in range(N):
    if j == 0:
        dp[0][j] = a[0][j]
        dp[1][j] = a[0][j] + a[1][j]
    else:
        dp[0][j] = dp[0][j - 1] + a[0][j]
        dp[1][j] = max(dp[1][j - 1] + a[1][j], dp[0][j] + a[1][j])
print((max(dp[1][-1], dp[0][-1])))
