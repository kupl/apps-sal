(n, a) = map(int, input().split())
x = list(map(int, input().split()))
for i in range(n):
    x[i] -= a
dp = [[0 for i in range(100 * n + 1)] for j in range(n + 1)]
dp[0][50 * n] = 1
for i in range(n):
    for j in range(100 * n + 1):
        j2 = j - 50 * n
        num = x[i]
        if -50 * n <= j2 - num <= 50 * n:
            dp[i + 1][j] = dp[i][j] + dp[i][j - num]
        else:
            dp[i + 1][j] = dp[i][j]
print(dp[n][50 * n] - 1)
