s = int(input())
dp = [0, 0, 0, 1]
x = 10**9 + 7
for i in range(4, s + 1):
    dp.append((dp[i - 1] + dp[i - 3]) % x)
print(dp[s])
