n, m = list(map(int, input().split()))
L = [False] * (n + 1)

for _ in range(m):
    a = int(input())
    L[a] = True

dp = [0] * (n + 1)
dp[0] = 1
MOD = 1000000007

for i in range(1, n + 1):
    if L[i]:
        continue
    if i == 1:
        dp[1] = 1
        continue
    dp[i] = dp[i - 1] + dp[i - 2]

print((dp[n] % MOD))
