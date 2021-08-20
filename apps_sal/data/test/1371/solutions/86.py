s = int(input())
dp = [0] * (s + 1)
mod = 10 ** 9 + 7
dp[0] = 1
for i in range(3, s + 1):
    dp[i] += sum(dp[:i - 2]) % mod
print(dp[-1])
