import copy
(N, M) = list(map(int, input().split()))
inf = 10 ** 9 + 7
dp = [[inf] * N for _ in range(N)]
for _ in range(M):
    (a, b, c) = list(map(int, input().split()))
    a -= 1
    b -= 1
    dp[a][b] = c
    dp[b][a] = c
old_dp = copy.deepcopy(dp)
check = [[False] * N for _ in range(N)]
count = 0
for k in range(N):
    for i in range(N):
        for j in range(N):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
count = 0
for i in range(N):
    for j in range(N):
        if old_dp[i][j] != dp[i][j] and old_dp[i][j] != inf:
            count += 1
print(count // 2)
