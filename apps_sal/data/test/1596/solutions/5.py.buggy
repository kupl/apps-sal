S = '*' + input()

if 'm' in S or 'w' in S:
    print(0)
    return

dp = [0] * (len(S) + 1)
dp[0] = 1
mod = 10**9 + 7

for i in range(1, len(S)):
    dp[i] = (dp[i] + dp[i - 1]) % mod
    if S[i] == 'u' and S[i - 1] == 'u' or S[i] == 'n' and S[i - 1] == 'n':
        dp[i + 1] = (dp[i + 1] + dp[i - 1]) % mod

print((dp[-1] + dp[-2]) % mod)
