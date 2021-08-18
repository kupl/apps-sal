mod1, mod2 = 10**9 + 7, 998244353
mod = mod1
dp = [0] * 13
dp[0] = 1
for i in input():
    if i == "?":
        dp = [sum(dp[4 * (j - k) % 13]for k in range(10)) % mod for j in range(13)]
    else:
        x = int(i)
        dp = [dp[4 * (j - x) % 13]for j in range(13)]

print(dp[5])
