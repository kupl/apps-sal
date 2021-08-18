N, M = map(int, input().split())
A = [0] * (N + 1)

for _ in range(M):
    a = int(input())
    A[a] = 1

dp = [0] * (N + 1)
dp[0] = 1
if A[1] == 0:
    dp[1] = 1

for i in range(2, N + 1):
    if A[i] == 0:
        dp[i] = dp[i - 1] + dp[i - 2]

print(dp[N] % 1000000007)
