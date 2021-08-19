from scipy.sparse.csgraph import floyd_warshall
import numpy as np
import sys
sdin = sys.stdin.readline

n = int(sdin())
graph = np.array([[0 for _ in range(n)] for _ in range(n)], dtype=float)
for i in range(n):
    graph[i] = np.array(list(map(int, sdin().split())))

# ワーシャルフロイドで最短距離出す
shortest = floyd_warshall(graph, directed=False)


if any([graph[i, j] != shortest[i, j] for i in range(n) for j in range(n)]):
    print(-1)

else:
    total = 0
    INF = float("inf")

    for i in range(n):
        graph[i, i] = INF

    for i in range(n):
        for j in range(i + 1, n):
            via_k = np.min(graph[i] + graph[j])

            if via_k > graph[i, j]:
                total += graph[i, j]

    print(int(total))
