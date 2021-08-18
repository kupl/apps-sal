N = int(input())
A = list(map(int, input().split()))
dp = [[] for _ in range(N + 1)]
dp[0].append(0)
for i in range(N):
    A[i] = [A[i], i + 1]
A.sort(reverse=True)
for M in range(1, N + 1):
    Ai, i = A[M - 1]
    dp[M].append(dp[M - 1][0] + Ai * (N - (M - 1) - i))
    for x in range(1, M):
        dp[M].append(max(dp[M - 1][x - 1] + Ai * (i - x), dp[M - 1][x] + Ai * (N - (M - x - 1) - i)))
    dp[M].append(dp[M - 1][M - 1] + Ai * (i - M))
print(max(dp[N]))
