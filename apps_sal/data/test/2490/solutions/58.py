s = input()
l = list(s)
l = [int(x) for x in l]
dp = [[0, 0] for i in range(len(s))]
dp[0][0] = l[0]
dp[0][1] = 11 - l[0]
for i in range(1, len(s)):
  dp[i][0] = min(dp[i - 1][0], dp[i - 1][1]) + l[i]
  dp[i][1] = min(dp[i - 1][0] + 11 - l[i], dp[i - 1][1] + 9 - l[i])
print((min(dp[-1][0], dp[-1][1])))

