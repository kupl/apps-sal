import math

n = int(input())

dp = [n] * (n + 1)

dp[0] = 0
dp[1] = 1

p = int(math.log(n, 6))
q = int(math.log(n, 9))

for i in range(1, n + 1):
    dp[i] = min(dp[i - 1] + 1, dp[i])
    for x in range(1, p + 10):
        y = pow(6, x)
        if i - y >= 0:
            dp[i] = min(dp[i - y] + 1, dp[i])
        else:
            break
    for x in range(1, q + 10):
        y = pow(9, x)
        if i - y >= 0:
            dp[i] = min(dp[i - y] + 1, dp[i])
        else:
            break

print(dp[n])
