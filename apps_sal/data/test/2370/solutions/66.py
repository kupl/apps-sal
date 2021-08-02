import numpy as np
from scipy.sparse.csgraph import floyd_warshall as wf
n = int(input())
s = np.array([list(map(int, input().split()))for i in range(n)])
if np.any(s != wf(s, directed=False)):
    print(-1)
else:
    c = 0
    for i in range(n):
        s[i][i] = 10**10
    for i in range(n):
        for j in range(i + 1, n):
            d = np.min(s[i] + s[j])
            if s[i, j] != d:
                c += s[i, j]
    else:
        print(c)
