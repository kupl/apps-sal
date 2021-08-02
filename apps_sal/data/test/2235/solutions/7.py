
n = int(input())
a = [0, ]
for i in range(n):
    x = int(input())
    a.append(x)

dp = [0] * (n + 1)
dp[0] = 0
p90 = 1
p1440 = 1
for i in range(1, n + 1):
    dp[i] = dp[i - 1] + 20
    while a[p90] + 90 <= a[i]:
        p90 = p90 + 1
    dp[i] = min(dp[i], dp[p90 - 1] + 50)
    while a[p1440] + 1440 <= a[i]:
        p1440 = p1440 + 1
    dp[i] = min(dp[i], dp[p1440 - 1] + 120)
for i in range(1, n + 1):
    print(dp[i] - dp[i - 1])
