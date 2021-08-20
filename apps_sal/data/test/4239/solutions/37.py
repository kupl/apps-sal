N = int(input())
dp = [N for i in range(N + 1)]
pow6 = [6 ** i for i in range(1, 8)]
pow9 = [9 ** i for i in range(1, 7)]
dp[0] = 0
for i in range(N + 1):
    dp[i] = min(dp[i], dp[i - 1] + 1)
    for j in pow6:
        if i - j >= 0:
            dp[i] = min(dp[i], dp[i - j] + 1)
    for j in pow9:
        if i - j >= 0:
            dp[i] = min(dp[i], dp[i - j] + 1)
print(dp[-1])
