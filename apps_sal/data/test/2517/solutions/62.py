from itertools import permutations as perm


def warshall(d, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]


(n, m, r) = map(int, input().split())
rr = [i - 1 for i in map(int, input().split())]
inf = float('INF')
route = [[inf for j in range(n)] for i in range(n)]
for _ in range(m):
    (a, b, c) = map(int, input().split())
    route[a - 1][b - 1] = route[b - 1][a - 1] = c
warshall(route, n)
ans = inf
for tmp in perm(rr):
    cost = 0
    for i in range(r - 1):
        cost += route[tmp[i]][tmp[i + 1]]
    if cost < ans:
        ans = cost
print(int(ans))
