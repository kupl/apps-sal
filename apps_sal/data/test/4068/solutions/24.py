n, m = list(map(int, input().split()))
broken = [False] * (n + 1)
for _ in range(m):
    broken[int(input())] = True

dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 1 if not broken[1] else 0
MOD = 10 ** 9 + 7

for i in range(2, n + 1):
    if not broken[i - 1]:
        dp[i] += (dp[i - 1])
    if not broken[i - 2]:
        dp[i] += (dp[i - 2])
    dp[i] %= MOD

print((dp[n]))

