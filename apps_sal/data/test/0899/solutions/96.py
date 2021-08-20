import sys
sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    (n, m) = list(map(int, input().split()))
    cost = [[f_inf] * n for _ in range(n)]
    for i in range(n):
        cost[i][i] = 0
    edge = []
    for _ in range(m):
        (a, b, c) = list(map(int, input().split()))
        cost[a - 1][b - 1] = c
        cost[b - 1][a - 1] = c
        edge.append([c, a - 1, b - 1])
    for k in range(n):
        for i in range(n):
            for j in range(n):
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
    res = 0
    for (d, x, y) in edge:
        if cost[x][y] < d:
            res += 1
    print(res)


def __starting_point():
    resolve()


__starting_point()
