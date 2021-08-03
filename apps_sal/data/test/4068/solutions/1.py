N, M = map(int, input().split())
a = [0] * (N + 1)
INF = 10**100
NUM = 7 + 10**9
dp = [0] * (N + 1)

for _ in range(M):
    tmp = int(input())
    a[tmp] = 1

dp[0] = 1
if not a[1]:
    dp[1] += dp[0]
for i in range(2, N + 1):
    if a[i]:
        continue
    dp[i] += dp[i - 1] + dp[i - 2]
    dp[i] %= NUM

print(dp[N])
