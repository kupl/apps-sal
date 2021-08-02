n = int(input())
s = input()
dp = [[0, 0, 0]for i in range(n)]
ct = 1
mod = 10**9 + 7
for i in range(n):
    if i == 0:
        if s[i] == '?': ct *= 3
        if s[i] == 'a' or s[i] == '?': dp[i][0] += 1
    else:
        aa, bb, cc = dp[i - 1]
        if s[i] == 'a':
            dp[i][0] = aa + ct
            dp[i][1] = bb
            dp[i][2] = cc
        if s[i] == 'b':
            dp[i][0] = aa
            dp[i][1] = aa + bb
            dp[i][2] = cc
        if s[i] == 'c':
            dp[i][0] = aa
            dp[i][1] = bb
            dp[i][2] = bb + cc
        if s[i] == '?':
            dp[i][0] = aa * 3 + ct
            dp[i][1] = bb * 3 + aa
            dp[i][2] = cc * 3 + bb
            ct *= 3
    ct %= mod
    dp[i][0] %= mod
    dp[i][1] %= mod
    dp[i][2] %= mod
print(dp[-1][-1])
