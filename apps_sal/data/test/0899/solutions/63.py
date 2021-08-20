import copy
INF = float('inf')


def warshall_floyd(d):
    n = len(d)
    wf = copy.deepcopy(d)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                wf[i][j] = min(wf[i][j], wf[i][k] + wf[k][j])
    return wf


(n, m) = list(map(int, input().split()))
d = [[INF] * n for i in range(n)]
edges = []
for i in range(m):
    (u, v, w) = list(map(int, input().split()))
    d[u - 1][v - 1] = w
    d[v - 1][u - 1] = w
    edges.append((u - 1, v - 1))
for i in range(n):
    d[i][i] = 0
fwd = warshall_floyd(d)
ret = 0
for (u, v) in edges:
    if fwd[u][v] < d[u][v]:
        ret += 1
print(ret)
