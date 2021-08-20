(mod1, mod2) = (10 ** 9 + 7, 998244353)
mod = mod2
(n, s) = map(int, input().split())
dp = [0] * (s + 1)
dp[0] = 1
for a in map(int, input().split()):
    dp = [(2 * dp[i] + (0 if i < a else dp[i - a])) % mod for i in range(s + 1)]
print(dp[-1])
