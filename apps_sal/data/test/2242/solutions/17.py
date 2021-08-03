S = input()
MOD = 2019
dp = [0] * MOD
dp[0] = 1
r = 0
t = 1
for c in reversed(S):
    r += int(c) * t
    r %= MOD
    t *= 10
    t %= MOD
    dp[r] += 1
print(sum(i * (i - 1) // 2 for i in dp))
