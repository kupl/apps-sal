import math
N = int(input())
dp = [0] * 100500
dp[1] = 1
for i in range(2, N + 1):
    dp[i] = dp[i - 1] + 1
    for j in range(math.floor(math.log(i, 6)) + 1):
        dp[i] = min(dp[i], dp[i - 6 ** j] + 1)
    for k in range(math.floor(math.log(i, 9) + 1e-08) + 1):
        dp[i] = min(dp[i], dp[i - 9 ** k] + 1)
print(dp[N])
