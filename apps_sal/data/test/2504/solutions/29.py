import sys
import numpy as np
from scipy.sparse.csgraph import csgraph_from_dense, floyd_warshall, csgraph_to_dense
from scipy.sparse import issparse
sys.setrecursionlimit(10**7)

n, m, l = [int(i) for i in sys.stdin.readline().split()]
graph = [[0 for i in range(n)] for j in range(n)]
for i in range(m):
    a, b, c = [int(i) for i in sys.stdin.readline().split()]
    a -= 1
    b -= 1
    graph[a][b] = c
    graph[b][a] = c

res = floyd_warshall(csgraph_from_dense(graph))
if issparse(res):
    res = csgraph_to_dense(res)
res = np.where(res <= l, 1, 0)
new_res = floyd_warshall(res)
new_res[new_res == np.inf] = 0
q = int(input())
for j in range(q):
    s, t = [int(i) for i in sys.stdin.readline().split()]
    s -= 1
    t -= 1
    dis = new_res[s, t]
    print(int(dis) - 1)
