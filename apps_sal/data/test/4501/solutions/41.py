n, a = list(map(int, input().split()))
x = list(map(int, input().split()))

x = [i - a for i in x]
dp = [[0] * n * 50 * 2 for i in range(n + 1)]

dp[0][n * 50] = 1

for i in range(n):
    for j in range(n * 50 * 2):
        t = j - x[i]
        if 0 <= t < n * 50 * 2:
            dp[i + 1][j] = dp[i][j] + dp[i][t]
        else:
            dp[i + 1][j] = dp[i][j]
print((dp[n][n * 50] - 1))
