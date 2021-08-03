n = int(input())
dp = [float('inf')] * (n + 1)
dp[0] = 0
for i in range(n + 1):
    for j in [6, 9]:
        cnt = 1
        while i + cnt <= n:
            if dp[i + cnt] > dp[i] + 1:
                dp[i + cnt] = dp[i] + 1
            cnt *= j
print(dp[-1])
