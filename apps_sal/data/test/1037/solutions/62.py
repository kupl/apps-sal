n = int(input())
a = list(map(int, input().split()))
a = list(zip(list(range(n)), a))
a.sort(key=lambda x: x[1])
dp = [[0 for i in range(n + 1)] for j in range(n + 1)]
ans = 0
for k in range(n):
    (i, ai) = a.pop()
    dp[k + 1][0] = dp[k][0] + ai * (i - k)
    dp[0][k + 1] = dp[0][k] + ai * (n - k - 1 - i)
    for l in range(k):
        dp[k - l][l + 1] = max(dp[k - l - 1][l + 1] + ai * (i - k + l + 1), dp[k - l][l] + ai * (n - l - 1 - i))
for k in range(n + 1):
    ans = max(ans, dp[k][n - k])
print(ans)
