n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    a[i] = (a[i], i)
b = sorted(a, reverse=True)
dp = [[-10 ** 14 for i in range(n + 1)] for j in range(n + 1)]
dp[0][0] = 0
for i in range(1, n + 1):
    see = b[i - 1][0]
    prv = b[i - 1][1]
    for j in range(i + 1):
        dp[j][i - j] = max(dp[j - 1][i - j] + abs(prv - (j - 1)) * see, dp[j][i - j - 1] + abs(n - i + j - prv) * see)
ans = 0
for i in range(n + 1):
    ans = max(ans, dp[i][n - i])
print(ans)
