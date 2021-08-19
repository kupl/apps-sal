import numpy as np
from scipy.sparse.csgraph import shortest_path, floyd_warshall
from scipy.sparse import csr_matrix
(N, M, R) = map(int, input().split())
r = list(map(int, input().split()))
r = list(map(lambda x: x - 1, r))
E = [[0 for j in range(N)] for i in range(N)]
for i in range(M):
    (a, b, c) = map(int, input().split())
    E[a - 1][b - 1] = c
    E[b - 1][a - 1] = c
E = np.array(E)
E = shortest_path(E, method='FW')
stack = []
for i in range(len(r)):
    stack.append([r[i], [], 0])
ans = 10 ** 18
while stack:
    (v, visited, dist) = stack.pop()
    if len(visited) != 0:
        dist += E[visited[-1]][v]
    visited2 = visited.copy()
    visited2.append(v)
    if len(visited2) == len(r):
        if dist < ans:
            ans = dist
        continue
    for i in range(len(r)):
        if r[i] not in visited2:
            stack.append([r[i], visited2, dist])
print(int(ans))
