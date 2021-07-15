def solve(k, length, MOD, div, dp):
    for i in range(1, k + 1):
        dp[0] = dp[0] * 25 * div * (length + i - 1) * pow(i, -1, MOD) % MOD
        dp[1] = (dp[1] + dp[0]) % MOD

    return(dp[1])


k = int(input())
s = input()
length = len(s)
MOD = 10**9 + 7
div = pow(26, -1, MOD)

dp = [pow(26, k, MOD)] * 2

print(solve(k, length, MOD, div, dp))
