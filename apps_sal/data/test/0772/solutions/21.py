G = [[1] * 5 for i in range(5)]

D = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]


def toggle(i, j):
    for d in D:
        G[i + d[0]][j + d[1]] = 1 - G[i + d[0]][j + d[1]]


for i in range(1, 4):
    n = list(map(int, input().split()))
    for j in range(1, 4):
        if n[j - 1] % 2 == 1:
            toggle(i, j)

for i in range(1, 4):
    for j in range(1, 4):
        print(G[i][j], end='')
    print()
