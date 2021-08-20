INF = 10 ** 9 + 7
(N, M) = map(int, input().split())
a = [int(input()) for _ in range(M)]
dp = [0] * (N + 1)
for i in range(M):
    dp[a[i]] = -1
dp[0] = 1
for i in range(1, N + 1):
    if dp[i] == -1:
        continue
    tmp = 0
    if dp[i - 1] != -1:
        tmp += dp[i - 1]
    if dp[i - 2] != -1 and i > 1:
        tmp += dp[i - 2]
    dp[i] = tmp % INF
print(dp[N])
