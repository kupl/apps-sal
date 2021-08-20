import numpy as np
(n, m) = map(int, input().split())
ab = []
for _ in range(n):
    (a, b) = map(int, input().split())
    ab.append((a, b))
result = np.zeros([m, n], dtype=np.int64)
cd = []
for i in range(m):
    (c, d) = map(int, input().split())
    for (j, (a, b)) in enumerate(ab):
        result[i, j] = abs(a - c) + abs(b - d)
print(*result.argmin(axis=0) + 1, sep='\n')
