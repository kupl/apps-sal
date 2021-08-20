(N, A) = map(int, input().split())
x = list(map(int, input().split()))
x = [i - A for i in x]
dp = [[0] * 50 * N * 2 for i in range(N + 1)]
dp[0][50 * N] = 1
for i in range(1, N + 1):
    for j in range(50 * N * 2):
        n = j - x[i - 1]
        if n >= 0 and n < 50 * N * 2:
            dp[i][j] = dp[i - 1][j] + dp[i - 1][n]
        else:
            dp[i][j] = dp[i - 1][j]
print(dp[N][50 * N] - 1)
