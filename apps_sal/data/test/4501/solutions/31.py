(n, a) = list(map(int, input().split()))
x = list(map(int, input().split()))
dp = [[[0] * 2550 for _ in range(55)] for _ in range(55)]
dp[0][0][0] = 1
for i in range(n):
    for j in range(n + 1):
        for sm in range(n * a + 1):
            if dp[i][j][sm] == 0:
                continue
            dp[i + 1][j][sm] += dp[i][j][sm]
            dp[i + 1][j + 1][sm + x[i]] += dp[i][j][sm]
ans = 0
for k in range(1, n + 1):
    ans += dp[n][k][a * k]
print(ans)
