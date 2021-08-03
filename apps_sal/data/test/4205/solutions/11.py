import numpy as np

N = int(input())
p = list(map(int, input().split()))

q = sorted(p)
p, q = np.array(p), np.array(q)

if np.sum(p != q) <= 2:
    print('YES')
else:
    print('NO')
