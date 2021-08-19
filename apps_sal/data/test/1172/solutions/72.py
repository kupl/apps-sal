s = input()
dp = [[0 for _ in range(4)] for _ in range(len(s))]
mod = 10 ** 9 + 7
power_3 = 1
for (idx, letter) in enumerate(s):
    dp[idx] = dp[idx - 1].copy()
    if letter == 'A':
        dp[idx][1] += power_3
    elif letter == 'B':
        dp[idx][2] += dp[idx - 1][1]
    elif letter == 'C':
        dp[idx][3] += dp[idx - 1][2]
    elif letter == '?':
        dp[idx][1] *= 3
        dp[idx][2] *= 3
        dp[idx][3] *= 3
        dp[idx][1] += power_3
        power_3 *= 3
        power_3 %= mod
        dp[idx][2] += dp[idx - 1][1]
        dp[idx][3] += dp[idx - 1][2]
        dp[idx][1] %= mod
        dp[idx][2] %= mod
        dp[idx][3] %= mod
print(dp[len(s) - 1][3] % mod)
