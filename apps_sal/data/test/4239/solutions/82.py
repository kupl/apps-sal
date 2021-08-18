n = int(input())

dp = [0] * (n + 10)

for i in range(n + 1):
    dp[i + 1] = dp[i] + 1


for i in range(1, n + 1):
    k = 6
    while k <= n:
        if i - k >= 0:
            dp[i] = min(dp[i], dp[i - k] + 1)
        k *= 6

    k = 9
    while k <= n:
        if i - k >= 0:
            dp[i] = min(dp[i], dp[i - k] + 1)

        k *= 9

print(dp[n])
