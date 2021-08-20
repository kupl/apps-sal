import sys
INF = float('inf')


def Bellmanford(n, edges, r):
    d = [INF] * n
    d[r] = 0
    for i in range(n):
        for (u, v, c) in edges:
            if d[u] != INF and d[u] + c < d[v]:
                d[v] = d[u] + c
                if i == n - 1 and v == n - 1:
                    return 'inf'
    return -d[n - 1]


(N, M) = map(int, sys.stdin.readline().split())
Edges = [None] * M
for i in range(M):
    (ai, bi, ci) = map(int, sys.stdin.readline().split())
    Edges[i] = (ai - 1, bi - 1, -ci)
ans = Bellmanford(N, Edges, 0)
print(ans)
