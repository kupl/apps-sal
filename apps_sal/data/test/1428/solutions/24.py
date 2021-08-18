import sys
input = sys.stdin.readline


N, M = map(int, input().split())
D = [list(map(int, input().split())) for _ in range(M)]
C = [list(map(int, input().split())) for _ in range(N)]

X = [[0 for _ in range(M)] for _ in range(3)]
for i in range(N):
    for j in range(N):
        x = (i + 1 + j + 1) % 3
        y = C[i][j] - 1
        X[x][y] += 1

Y = [[0 for _ in range(M)] for _ in range(3)]
for i in range(3):
    for c_to in range(M):
        total = 0
        for c_from in range(M):
            total += X[i][c_from] * D[c_from][c_to]
        Y[i][c_to] = total

ans = 10**10
for i in range(M):
    for j in range(M):
        for k in range(M):
            if i != j and j != k and k != i:
                ans = min(ans, Y[0][i] + Y[1][j] + Y[2][k])

print(ans)
