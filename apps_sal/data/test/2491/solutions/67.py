import sys
INF = float('inf')


def Bellmanford(n, edges, r):
    d = [INF] * n
    d[r] = 0
    for i in range(n):
        for (u, v, c) in edges:
            if d[u] != INF and d[v] > d[u] + c:
                d[v] = d[u] + c
                if i == n - 1 and v == n - 1:
                    return 'inf'
    return -1 * d[n - 1]


(n, m) = map(int, input().split())
edges = [0] * m
for i in range(m):
    (a, b, c) = map(int, input().split())
    edges[i] = (a - 1, b - 1, -c)
ans = Bellmanford(n, edges, 0)
print(ans)
