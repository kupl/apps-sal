(n, m) = (int(x) for x in input().split())
A = sorted([int(x) for x in input().split()])[::-1]
cost = (0, 2, 5, 5, 4, 5, 6, 3, 7, 6)
dp = [[0] * (n + 1) for _ in range(m + 1)]
for i in range(m):
    for j in range(1, n + 1):
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
        if j >= cost[A[i]]:
            if dp[i + 1][j - cost[A[i]]] == 0:
                if j == cost[A[i]]:
                    dp[i + 1][j] = max(A[i], dp[i][j])
                else:
                    dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            else:
                dp[i + 1][j] = max(dp[i + 1][j], 10 * dp[i + 1][j - cost[A[i]]] + A[i])
print(dp[m][n])
