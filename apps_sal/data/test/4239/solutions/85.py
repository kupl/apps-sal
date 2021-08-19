N = int(input())
dp = [N] * (N + 1)
dp[0] = 0
for i in range(1, N + 1):
    dp[i] = dp[i - 1] + 1
    for k in range(1, 10):
        if i < 6 ** k:
            break
        else:
            dp[i] = min(dp[i], dp[i - 6 ** k] + 1)
    for k in range(1, 10):
        if i < 9 ** k:
            break
        else:
            dp[i] = min(dp[i], dp[i - 9 ** k] + 1)
print(dp[N])
