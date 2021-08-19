import numpy as np
from collections import defaultdict
(n, w) = map(int, input().split())
D = defaultdict(list)


def warshall_floyd(d):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]
                    D[i, j] = D[i, k] + D[k, j][1:]
    return d


done = [[-1] * n for _ in range(n)]
d = [[float('inf')] * n for i in range(n)]
for i in range(w):
    (x, y, z) = map(int, input().split())
    d[x - 1][y - 1] = z
    d[y - 1][x - 1] = z
    D[x - 1, y - 1] = [x - 1, y - 1]
    D[y - 1, x - 1] = [y - 1, x - 1]
    done[x - 1][y - 1] = 0
    done[y - 1][x - 1] = 0
for i in range(n):
    d[i][i] = 0
warshall_floyd(d)
for l in D.values():
    for i in range(1, len(l)):
        a = l[i - 1]
        b = l[i]
        done[a][b] = 1
        done[b][a] = 1
done = np.array(done)
ans = (done == 0).sum()
print(ans // 2)
