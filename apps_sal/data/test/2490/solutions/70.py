n = input()
len_n = len(n)
dp = [[0,2] for i in range(len_n+1)]
for k,v in enumerate(n[::-1]):
    v = int(v)
    dp[k+1][0] = min(dp[k][0] + v, dp[k][1] + v)
    dp[k+1][1] = min(dp[k][0] + 10 - v + 1, dp[k][1] + 10 - v - 1)
print((min(dp[len_n])))

