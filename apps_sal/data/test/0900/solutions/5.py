S = [int(x) if x != "?" else -1 for x in input()]
mod = int(1e9 + 7)
r = [0] * 13
if S[0] != -1:
    r[S[0]] = 1
else:
    for i in range(10):
        r[i] = 1
for i in range(1, len(S)):
    dp = [0] * 26
    for j in range(13):
        dp[j * 10 % 13] += (r[j] % mod)

    dp[13:26] = dp[0:13]
    r = [0] * 13
    if S[i] == -1:
        s = sum(dp[4:14])
        for j in range(13):
            r[j] += s
            s += dp[j + 1] - dp[4 + j]
    else:
        for j in range(13):
            r[j] += dp[13 - S[i] + j]
print(r[5] % mod)
