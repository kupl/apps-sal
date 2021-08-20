import numpy as np
from scipy.sparse.csgraph import shortest_path
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse.csgraph import csgraph_from_dense
INF = float('inf')


def main():
    (N, M, L) = map(int, input().split())
    G = [[INF] * (N + 1) for n in range(N + 1)]
    for i in range(M):
        (a, b, c) = map(int, input().split())
        G[a][b] = c
        G[b][a] = c
    G = csgraph_from_dense(G, null_value=INF)
    Q = int(input())
    Queries = []
    for i in range(Q):
        (s, t) = map(int, input().split())
        Queries.append((s, t))
    cost = floyd_warshall(G)
    no_refuel = [[1 if x <= L else INF for x in c] for c in cost]
    no_refuel = csgraph_from_dense(no_refuel, null_value=INF)
    refuel_count = floyd_warshall(no_refuel)
    ans = []
    for (s, t) in Queries:
        d = refuel_count[s][t]
        ans.append(int(d - 1) if d != INF else -1)
    print(*ans, sep='\n')


def __starting_point():
    main()


__starting_point()
