n, m, k = list(map(int, input().strip().split()))

a = list(map(int, input().strip().split()))
a = [0] + a
dp = [0] * 300005
ans = 0
for i in range(1, n + 1):
    a[i] += a[i - 1]
    for j in range(1, m + 1):
        if i - j >= 0:
            dp[i] = max(dp[i], a[i] - a[i - j] - k)
    if i - m >= 0:
        dp[i] = max(dp[i], a[i] - a[i - m] + dp[i - m] - k)
    ans = max(ans, dp[i])

print(ans)

