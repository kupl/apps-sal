
N = int(input())
A = list(map(int, input().split()))
A = [[A[i], i] for i in range(N)]
A.sort(reverse=True)
dp = [[0] * (N + 1) for _ in range(N + 1)]


dp[0][0] = 0
for x in range(1, N + 1):
    dp[x][0] = dp[x - 1][0] + A[x - 1][0] * (A[x - 1][1] - x + 1)
for y in range(1, N + 1):
    dp[0][y] = dp[0][y - 1] + A[y - 1][0] * (N - y - A[y - 1][1])

for x in range(1, N):
    for y in range(1, N + 1 - x):
        A0 = A[x + y - 1][0]
        A1 = A[x + y - 1][1]
        dp[x][y] = max(dp[x - 1][y] + A0 * (A1 + 1 - x), dp[x][y - 1] + A0 * (N - y - A1))


c = 0
for i in range(N):
    if c < dp[i][N - i]:
        c = dp[i][N - i]
print(c)
