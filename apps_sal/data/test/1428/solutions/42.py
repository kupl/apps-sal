N, C = list(map(int, input().split()))
D = [0] * C
for i in range(C):
    D[i] = list(map(int, input().split()))
grid = [0] * N
for i in range(N):
    grid[i] = list(map(int, input().split()))

grid3 = [[0] * C for i in range(3)]
for i in range(N):
    for j in range(N):
        nn = (i + j) % 3
        color = grid[i][j] - 1
        grid3[nn][color] += 1

score = [[0] * C for i in range(3)]
for j in range(C):
    for i in range(3):
        for k in range(C):
            score[i][j] += grid3[i][k] * D[k][j]
ans = 10 ** 10
for i in range(C):
    for j in range(C):
        if i != j:
            for k in range(C):
                if (i != k) and (j != k):
                    now = score[0][i] + score[1][j] + score[2][k]
                    ans = min(ans, now)
print(ans)
