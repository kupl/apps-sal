import numpy as np
(n, k, q) = map(int, input().split())
a = np.array([k] * n)
a -= q
for i in range(q):
    a[int(input()) - 1] += 1
for i in range(n):
    if a[i] > 0:
        print('Yes')
    else:
        print('No')
