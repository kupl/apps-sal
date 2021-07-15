n = int(input())
dp = [0] * 5000
MOD = 10 ** 9 + 7
f = 1
dp[0] = 1
for i in range(n):
    a = input()
    if a == "f":
        f += 1
    else:
        for j in range(1, f):
            dp[j] = dp[j] + dp[j - 1]
            dp[j] %= MOD

print(dp[f - 1])
