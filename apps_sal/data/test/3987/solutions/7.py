R = lambda: map(int, input().split())
n = int(input())
dp = [0] * 5
for x in R():
    if x == 1:
        dp[1], dp[3] = dp[1] + 1, max(dp[3], dp[2]) + 1
    else:
        dp[2], dp[4] = max(dp[1], dp[2]) + 1, max(dp[3], dp[4]) + 1
print(max(dp))
