from itertools import accumulate
import numpy as np
(n, m, q) = list(map(int, input().split()))
lr = [list(map(int, input().split())) for _ in range(m)]
pq = [list(map(int, input().split())) for _ in range(q)]
data = [[0] * 500 for i in range(500)]
for (l, r) in lr:
    data[l - 1][r - 1] += 1
data = np.array(data)
data = np.cumsum(data, axis=1)
data = np.cumsum(data, axis=0)
for (p, q) in pq:
    ans = 0
    if p == 1:
        ans = data[q - 1][q - 1]
    else:
        ans = data[q - 1][q - 1] - data[p - 1 - 1][q - 1]
    print(ans)
