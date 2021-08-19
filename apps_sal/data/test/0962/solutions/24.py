import numpy as np
from scipy.sparse.csgraph import dijkstra


def get_path(start, goal, pred):
    return get_path_row(start, goal, pred[start])


def get_path_row(start, goal, pred_row):
    path = []
    i = goal
    while i != start and i >= 0:
        path.append(i)
        i = pred_row[i]
    if i < 0:
        return []
    path.append(i)
    return path[::-1]


(N, M) = map(int, input().split())
g = [[np.inf] * (2 * N) for _ in range(2 * N)]
for i in range(M):
    (a, b) = map(int, input().split())
    a -= 1
    b -= 1
    g[a][b] = 1
    g[a][b + N] = 1
    g[a + N][b] = 1
ans = np.inf
j = -1
d = dijkstra(g, return_predecessors=True)
for i in range(N):
    if d[0][i][i + N] < ans:
        ans = int(d[0][i][i + N])
        j = i
if ans != np.inf:
    path = get_path(j, j + N, d[1])[::-1][:-1]
    path = [node % N for node in path]
    print(ans)
    for node in path:
        print(node + 1)
else:
    print(-1)
