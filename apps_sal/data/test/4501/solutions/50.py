n, a = map(int, input().split())
X = list(map(int, input().split()))
dp = [[0] * 2501 for _ in range(n + 1)]
dp[0][0] = 1
for i in range(n):
    x = X[i]
    for j in range(n, 0, -1):
        for k in range(2501 - x):
            dp[j][k + x] += dp[j - 1][k]
ans = 0
for i in range(n):
    ans += dp[i + 1][(i + 1) * a]
print(ans)
