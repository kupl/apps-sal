n, k, x = list(map(int, input().split()))
a = [None] + list(map(int, input().split()))
dp = [[-1] * (n + 1) for i in range(x + 1)]
dp[0][0] = 0
for i in range(1, x + 1):
    for j in range(1, n + 1):
        dp[i][j] = max(dp[i - 1][j2] for j2 in range(max(0, j - k), j))
        if dp[i][j] != -1:
            dp[i][j] += a[j]
ans = max(dp[x][j] for j in range(n - k + 1, n + 1))
print(ans)
