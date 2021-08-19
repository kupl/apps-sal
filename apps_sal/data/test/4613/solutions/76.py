from scipy.sparse.csgraph import floyd_warshall
import numpy as np
(N, M) = (int(x) for x in input().split())
edge = [tuple((int(x) for x in input().split())) for _ in range(M)]
INF = 100
tmpl_graph = [[INF if i != j else 0 for j in range(N)] for i in range(N)]
ans = 0
for E in edge:
    edgeWithoutE = edge.copy()
    edgeWithoutE.remove(E)
    graph = np.array(tmpl_graph)
    for x in edgeWithoutE:
        graph[x[0] - 1, x[1] - 1] = 1
        graph[x[1] - 1, x[0] - 1] = 1
    graph = floyd_warshall(graph, directed=False)
    if len(graph[graph == 100]) > 0:
        ans += 1
print(ans)
