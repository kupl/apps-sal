N, M = map(int, input().split())
DP = [[float('inf')] * N for _ in range(N)]
B = []
for i in range(N):
    DP[i][i] = 0
for _ in range(M):
    a, b, c = map(int, input().split())
    DP[a - 1][b - 1] = c
    DP[b - 1][a - 1] = c
    B.append([a - 1, b - 1, c])
for k in range(N):
    for i in range(N):
        for j in range(N):
            DP[i][j] = min(DP[i][j], DP[i][k] + DP[k][j])
ans = 0
for i in range(M):
    a, b, c = B[i]
    for j in range(N):
        if DP[j][b] == DP[j][a] + c:
            break
    else:
        ans += 1
print(ans)
