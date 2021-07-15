n = int(input())
d = len(bin(n)) - 2
mod = 10**9 + 7
dp = [[0 for j in range(3)] for i in range(d+1)]
dp[d][0] = 1
for i in range(d):
    k = d - 1 - i
    for j in range(3):
        if j == 0:
            if (n >> k) & 1:
                dp[k][0] += dp[k+1][0]
                dp[k][1] += dp[k+1][0]
            else:
                dp[k][0] += dp[k+1][0]
        elif j == 1:
            if (n >> k) & 1:
                dp[k][1] += dp[k+1][1]
                dp[k][2] += dp[k+1][1] * 2
            else:
                dp[k][0] += dp[k+1][1]
                dp[k][1] += dp[k+1][1]
                dp[k][2] += dp[k+1][1]
        else:
            dp[k][2] += dp[k+1][2] * 3
        map(lambda x:x%mod, dp[k])
print(sum(dp[0]) % mod)
