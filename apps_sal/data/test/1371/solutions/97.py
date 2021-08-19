s = int(input())

mod = 10 ** 9 + 7

maxV = 2000
dp = [0] * (maxV + 1)

for i in range(s + 1):
    if i == 0:
        dp[i] = 1
        continue
    elif 0 < i < 3:
        dp[i] = 0
        continue
    # for j in range(i-3 + 1):
    #     dp[i] += (dp[j]) % mod
    dp[i] = (dp[i - 1] + dp[i - 3]) % mod

print((dp[s] % mod))
