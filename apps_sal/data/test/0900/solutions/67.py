

s = input()
l = len(s)
dp = [[0 for _ in range(13)] for _ in range(l + 1)]
dp[0][0] = 1
temp = [0] * 13
summ = 1
mod = 10 ** 9 + 7

for i in range(0, l):
    if s[i] != '?':
        for k in range(13):
            dp[i + 1][(k * 10 + int(s[i])) % 13] = dp[i][k]
    else:
        for k in range(13):
            temp[(k * 10) % 13] = dp[i][k]

        excluded = temp[1] + temp[2] + temp[3]
        for k in range(13):
            dp[i + 1][k] = (summ - excluded) % mod
            excluded -= temp[(k + 1) % 13]
            excluded += temp[(k + 4) % 13]

        summ *= 10
        summ %= mod

print((dp[l][5]))
