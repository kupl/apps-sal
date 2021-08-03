MOD = 1000000007

s = [int(x) if x != "?" else -1 for x in input()]

n = len(s)

r = [0] * 13

c = s[0]
if (c != -1):
    r[c] = 1
else:
    for i in range(10):
        r[i] = 1

for i in range(1, n):
    dp = [0] * 26
    for j in range(13):
        dp[j * 10 % 13] += (r[j] % MOD)
    dp[13:26] = dp[0:13]
    c = s[i]
    r = [0] * 13
    if (c == -1):
        w = sum(dp[4:14])
        for j in range(13):
            r[j] += w
            w = w + dp[j + 1] - dp[4 + j]
    else:
        for j in range(13):
            r[j] += dp[13 - c + j]
print((r[5] % MOD))
