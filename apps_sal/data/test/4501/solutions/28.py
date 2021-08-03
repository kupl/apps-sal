n, a, = map(int, input().split())
x = list(map(lambda y: int(y) - a, input().split()))
w = 2 * n * (max(max(x), a))
dp = [[0] * (w + 1) for _ in range(n + 1)]
dp[0][w // 2] = 1
for i in range(1, n + 1):
    for j in range(w + 1):
        dp[i][j] = dp[i - 1][j] + (dp[i - 1][j - x[i - 1]] if 0 <= j - x[i - 1] <= w else 0)
print(dp[n][w // 2] - 1)
