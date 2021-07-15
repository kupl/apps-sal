# D - AtCoder Express 2

N, M, Q = map(int, input().split())
G = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    L, R = map(int, input().split())
    G[L][R] += 1

for i in range(N):
    for j in range(N):
        G[i+1][j+1] += G[i+1][j] + G[i][j+1] - G[i][j]

for _ in range(Q):
    p, q = map(int, input().split())
    ans = G[q][q] - G[p-1][q] - G[q][p-1] + G[p-1][p-1]
    print(ans)
