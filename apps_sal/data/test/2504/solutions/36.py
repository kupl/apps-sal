import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra
(n, m, l) = list(map(int, input().split()))
abc = []
for _ in range(m):
    abc.append(list(map(int, input().split())))
q = int(input())
st = []
for _ in range(q):
    st.append(list(map(int, input().split())))
adjacency_matrix = np.zeros((n, n))
for (a, b, c) in abc:
    adjacency_matrix[a - 1, b - 1] = c
    adjacency_matrix[b - 1, a - 1] = c
shotest = dijkstra(adjacency_matrix)
fuel_once = np.where(shotest <= l, 1, 0)
fuel_times = dijkstra(fuel_once - np.eye(n))
for (s, t) in st:
    ans = fuel_times[s - 1][t - 1]
    if np.isinf(ans):
        print(-1)
    else:
        print(int(ans) - 1)
