import numpy as np

n, m, x, y = list(map(int, input().split()))
px = np.array([int(i) for i in input().split()])
py = np.array([int(i) for i in input().split()])

res = 'War'
for i in range(x+1, y+1):
    if np.count_nonzero(px < i) == n and np.count_nonzero(py >= i) == m:
        res = 'No War'
        break
print(res)

