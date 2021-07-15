n = int(input())
p = list(map(float, input().split()))
p.sort()
dp = [[0.0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    dp[i][i] = 1.0 - p[i]
    for j in range(i + 1, n):
        dp[i][j] = dp[i][j - 1] * (1.0 - p[j])

ans = p[-1]
for i in range(n):
    for j in range(i + 1, n):
        prob = 0
        for k in range(i, j + 1):
            if k == i:
                prob += p[i] * dp[i + 1][j]
            elif k == j:
                prob += p[j] * dp[i][j - 1]
            else:
                prob += dp[i][k - 1] * p[k] * dp[k + 1][j]

        ans = max(ans, prob)

print(ans)


