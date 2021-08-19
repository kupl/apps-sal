import numpy as np
from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson
from scipy.sparse import csr_matrix
(n, m) = map(int, input().split())
ma = [[0] * n for _ in range(n)]
list_ABC = [list(map(int, input().split(' '))) for i in range(m)]
for (a, b, c) in list_ABC:
    ma[a - 1][b - 1] = c
    ma[b - 1][a - 1] = c
x = csr_matrix(ma)
y = dijkstra(x, directed=False).astype(int)
ans = 0
for (a, b, c) in list_ABC:
    if y[a - 1][b - 1] != c:
        ans += 1
print(ans)
