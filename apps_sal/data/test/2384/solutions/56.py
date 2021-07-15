n = int(input())
a = list(map(int, input().split()))
a.insert(0, 0)
dp = [[0] * (n + 1) for _ in range(3)]
for i in range(n % 2 + 2):
    for j in range(1 + i, n + i, 2):
        if i == 0:
            if j == 1:
                dp[i][j] = a[j]
            else:
                dp[i][j] = dp[i][j - 2] + a[j]
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i][j - 2] + a[j])
ans = dp[n % 2 + 1][n]
print(ans)
