n, a = map(int, input().split())
x = list(map(int, input().split()))
dp = [[0] * (n * a + 1) for i in range(n + 1)]
dp[0][0] = 1
ans = 0
for i in x:
    for j in range(n, 0, -1):
        for k in range(n * a, i - 1, -1):
            dp[j][k] += dp[j - 1][k - i]
for i in range(1, n + 1):
    ans += dp[i][i * a]
print(ans)
