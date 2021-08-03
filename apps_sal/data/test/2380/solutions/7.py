import numpy as np

n, m = map(int, input().split())
a = np.array(sorted(list(map(int, input().split()))), dtype=np.int64)
bc = sorted([list(map(int, input().split())) for _ in range(m)], key=lambda x: -x[1])

p = 0
for b, c in bc:
    a[p:p + b] = np.maximum(a[p:p + b], c)
    p += b
print(np.sum(a))
