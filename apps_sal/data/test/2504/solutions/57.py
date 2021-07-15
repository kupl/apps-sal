from scipy.sparse.csgraph import floyd_warshall
import numpy as np

N, M, L = list(map(int, input().split()))
graph = np.array([[0 if i == j else float("inf")
                   for i in range(N)] for j in range(N)])
graph2 = np.array([[0 if i == j else float("inf")
                   for i in range(N)] for j in range(N)])


for _ in range(M):
    a, b, c = list(map(int, input().split()))
    graph[a - 1][b - 1] = c
    graph[b - 1][a - 1] = c
dist = floyd_warshall(graph)

graph2[(dist <= L) & (dist != 0)] = 1
dist2 = floyd_warshall(graph2)
dist2[dist2 == float("inf")] = 0

Q = int(input())
for _ in range(Q):
    s, t = list(map(int, input().split()))
    print((int(dist2[s - 1, t - 1]) - 1))


