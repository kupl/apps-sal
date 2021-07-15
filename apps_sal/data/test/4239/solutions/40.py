N = int(input())
dp = [0] * 10 ** 6
for i in range(1, N + 1):
    power = 6
    dp[i] = i
    while power <= i:
        dp[i] = min(dp[i], dp[i - power] + 1)
        power *= 6
    power = 9
    while power <= i:
        dp[i] = min(dp[i], dp[i - power] + 1)
        power *= 9
print(dp[N])
