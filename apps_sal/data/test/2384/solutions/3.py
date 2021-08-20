N = int(input())
A = list(map(int, input().split()))
inf = 10 ** 18
x = N % 2 + 1
dp = [[-inf] * 4 for _ in range(N + 10)]
dp[0][0] = 0
for (i, a) in enumerate(A):
    for j in range(x + 1):
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j])
        now = dp[i][j]
        if (i + j) % 2 == 0:
            now += a
        dp[i + 1][j] = max(dp[i + 1][j], now)
print(dp[N][x])
