import math

n = int(input())
t = 100000 + 10

dp = [10**18] * (t+10)
dp[0] = 0

for i in range(1, t+1):
    dp[i] = dp[i-1] + 1

for i in range(t-1):
    s = t-i
    for j in range(int(math.log(s, 9)+1)):
        dp[i+9**j] = min(dp[i+9**j], dp[i]+1)
    for k in range(int(math.log(s, 6)+1)):
        dp[i+6**k] = min(dp[i+6**k], dp[i]+1)


print(dp[n])
