N, M = map(int, input().split())
Edge = [tuple(map(int, input().split())) for _ in range(M)]

import numpy as np
Graph = np.array([[0 if i == j else np.inf for i in range(N)] for j in range(N)])
for a,b,c in Edge:
    Graph[a-1,b-1] = c
from scipy.sparse.csgraph import dijkstra 
Graph = dijkstra(Graph,directed=False)
ans = 0
for a,b,c in Edge:
    if Graph[a-1,b-1] != c:
        ans += 1
print(ans)
