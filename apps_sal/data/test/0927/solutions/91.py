(N, M) = map(int, input().split())
A = list(map(int, input().split()))
C = [0, 1, 4, 4, 3, 4, 5, 2, 6, 5]
dp = N * [0] + 9 * [-1]
for n in range(N):
    dp[n + 1] = max((a + 10 * dp[n - C[a]] for a in A))
print(dp[N])
