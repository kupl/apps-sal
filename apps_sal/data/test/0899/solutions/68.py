# 051_D
inf = 10 ** 10
n, m = map(int, input().split())
d = [[inf for _ in range(n)] for _ in range(n)]
for i in range(n):
    d[i][i] = 0
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    d[a - 1][b - 1] = c
    d[b - 1][a - 1] = c
    edges.append((a - 1, b - 1, c))


def warshall_floyd(d):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])


warshall_floyd(d)

ans = m
for u, v, c in edges:
    flg = False
    for i in range(n):
        if d[i][v] + c == d[i][u]:
            flg = True

    if flg:
        ans -= 1

print(ans)
