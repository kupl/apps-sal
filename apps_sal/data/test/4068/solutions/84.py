n, m = list(map(int, input().split()))
is_safe = [True] * (n + 1)
for _ in range(m):
    is_safe[int(input())] = False

MOD = 10**9 + 7
dp = [0] * (n + 1)
dp[0] = 1
if is_safe[1]:
    dp[1] = 1

for i in range(2, n + 1):
    if is_safe[i - 1]:
        dp[i] += dp[i - 1]
    if is_safe[i - 2]:
        dp[i] += dp[i - 2]
    dp[i] %= MOD

print((dp[n]))
