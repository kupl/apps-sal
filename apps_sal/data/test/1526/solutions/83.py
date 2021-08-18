import numpy as np

A, B, C = list(map(int, input().split()))


vals = np.array([A, B, C])
vals = np.sort(vals)

sumval = vals.sum()


cn = vals[-1] + np.sum(vals[:2]) % 2

n = (3 * cn - sumval) // 2

print(n)
