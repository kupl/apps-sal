s = input()
n = len(s)
mod = 2019

t = [0] * n
dp = [0] * 2020
t[0] = int(s[-1])
dp[t[0]] += 1
for i in range(n - 1):
    t[i + 1] = t[i] + int(s[-2 - i]) * pow(10, i + 1, mod)
    t[i + 1] %= mod
    dp[t[i + 1]] += 1
ans = 0
for D in dp[1:]:
    ans += D * (D - 1) // 2
print((ans + (dp[0] + 1) * (dp[0]) // 2))
