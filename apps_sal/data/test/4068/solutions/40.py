N, M = map(int, input().split())
a = set([int(input()) for _ in range(M)])
INF = 1000000007

dp = [0] * (N + 1)
dp[0] = 1
if 1 not in a:
    dp[1] = 1
else:
    dp[1] = 0
for i in range(2, N + 1):
    if i in a:
        continue
    dp[i] = dp[i - 1] + dp[i - 2]
    dp[i] %= INF

print(dp[N])
