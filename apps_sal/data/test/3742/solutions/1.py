n = int(input())
a = list(map(int, input().split()))
INF = 10 ** 5
dp = [[[INF] * (n + 1) for i in range(n + 1)] for i in range(2)]
dp[0][0][0] = 0
dp[1][0][0] = 0
for i in range(n):
    if a[i] != 0:
        parity = a[i] % 2
        if parity % 2 == 0:
            for j in range(n + 1):
                dp[0][i + 1][j] = min(dp[0][i][j], dp[0][i + 1][j])
                dp[0][i + 1][j] = min(dp[1][i][j] + 1, dp[0][i + 1][j])
        if parity % 2 == 1:
            for j in range(n):
                dp[1][i + 1][j + 1] = min(dp[1][i][j], dp[1][i + 1][j + 1])
                dp[1][i + 1][j + 1] = min(dp[0][i][j] + 1, dp[1][i + 1][j + 1])
    else:
        for j in range(n + 1):
            dp[0][i + 1][j] = min(dp[0][i][j], dp[0][i + 1][j])
            dp[0][i + 1][j] = min(dp[1][i][j] + 1, dp[0][i + 1][j])
        for j in range(n):
            dp[1][i + 1][j + 1] = min(dp[1][i][j], dp[1][i + 1][j + 1])
            dp[1][i + 1][j + 1] = min(dp[0][i][j] + 1, dp[1][i + 1][j + 1])
odd_cnt = (n + 1) // 2
even_cnt = n // 2
print(min(dp[1][n][odd_cnt], dp[0][n][odd_cnt]))
