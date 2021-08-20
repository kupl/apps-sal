(n, a) = map(int, input().split())
x = [int(x) for x in input().split()]
dp = [[0] * 2501 for _ in range(n + 1)]
for i in range(n + 1):
    for j in range(i - 1, -1, -1):
        if j == 0:
            dp[j + 1][x[i - 1]] += 1
        for k in range(2500, -1, -1):
            if dp[j][k] and k + x[i - 1] <= 2500:
                dp[j + 1][k + x[i - 1]] += dp[j][k]
ans = 0
for i in range(1, n + 1):
    ans += dp[i][i * a]
print(ans)
