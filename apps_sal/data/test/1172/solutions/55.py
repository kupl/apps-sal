S = input()
MOD = 10**9 + 7
dp = [[0, 0, 0] for i in range(len(S) + 1)]

base = 1
for i, s in enumerate(S, 1):
    dp[i][0] = dp[i - 1][0]
    dp[i][1] = dp[i - 1][1]
    dp[i][2] = dp[i - 1][2]
    if s == 'A':
        dp[i][0] += base
        dp[i][0] %= MOD
    elif s == 'B':
        dp[i][1] += dp[i - 1][0]
        dp[i][1] %= MOD
    elif s == 'C':
        dp[i][2] += dp[i - 1][1]
        dp[i][2] %= MOD
    else:
        dp[i][0] += 2 * dp[i - 1][0] + base
        dp[i][1] += 2 * dp[i - 1][1] + dp[i - 1][0]
        dp[i][2] += 2 * dp[i - 1][2] + dp[i - 1][1]
        dp[i][0] %= MOD
        dp[i][1] %= MOD
        dp[i][2] %= MOD
        base *= 3
        base %= MOD

print(dp[-1][2])
