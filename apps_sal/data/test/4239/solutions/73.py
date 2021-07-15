n = int(input())
dp = [float('inf')]*100100
dp[0] = 0

for i in range(len(dp)):
    power = 1
    while power <= n:
        dp[i] = min(dp[i], dp[i-power]+1)
        power *= 6

    power = 1
    while power <= n:
        dp[i] = min(dp[i], dp[i-power]+1)
        power *= 9

print(dp[n])
