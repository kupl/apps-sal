from itertools import permutations
(N, C) = map(int, input().split())
D = []
for _ in range(C):
    Ds = list(map(int, input().split()))
    D.append(Ds)
grid = []
for _ in range(N):
    c = list(map(lambda x: int(x) - 1, input().split()))
    grid.append(c)
color = [[0] * C for _ in range(3)]
for i in range(N):
    for j in range(N):
        color[(i + j) % 3][grid[i][j]] += 1
INF = 10 ** 9
ans = INF
for cols in permutations(range(C), 3):
    temp = 0
    for (i, Y) in enumerate(cols):
        for (X, cnt) in enumerate(color[i]):
            temp += D[X][Y] * cnt
    ans = min(ans, temp)
print(ans)
