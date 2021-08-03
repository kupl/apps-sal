import sys
readline = sys.stdin.readline

N = readline()
S = readline().strip()
mod = 10**9 + 7
dp = [1] + [0] * 3
for s in S:
    dp1 = dp[:]
    if s == 'a':
        dp1[1] += dp[0]
    elif s == 'b':
        dp1[2] += dp[1]
    elif s == 'c':
        dp1[3] += dp[2]
    else:
        dp1[1] += dp[0]
        dp1[2] += dp[1]
        dp1[3] += dp[2]
        dp1[0] += 2 * dp[0]
        dp1[1] += 2 * dp[1]
        dp1[2] += 2 * dp[2]
        dp1[3] += 2 * dp[3]
    dp = [d % mod for d in dp1]
print(dp[-1])
