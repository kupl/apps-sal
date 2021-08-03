from math import inf


n = int(input())
A = list(map(int, input().split()))

dp = [[-inf] * 3 for _ in range(n + 1)]
k = 1 + n % 2
dp[0][0] = 0
for i in range(n):
    for j in range(k + 1):
        if j < k:
            dp[i + 1][j + 1] = dp[i][j]
        now = dp[i][j]
        if (i + j) % 2 == 0:
            now += A[i]
        dp[i + 1][j] = max(dp[i + 1][j], now)
print((dp[n][k]))
