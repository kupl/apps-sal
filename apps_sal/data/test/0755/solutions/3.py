dp = [0] * 1000005
x = int(input())
dp[0] = 0
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 1
dp[5] = 1
for i in range(6, 1000001):
    dp[i] = min([dp[i-1], dp[i-2], dp[i-3], dp[i-4], dp[i-5]])+1
print(dp[x])

