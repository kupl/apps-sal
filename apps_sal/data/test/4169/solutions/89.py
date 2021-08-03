import numpy as np
n, m = map(int, input().split())
A = np.array([list(map(int, input().split())) for _ in range(n)], dtype='int64')
ind = np.argsort(A[:, 0])
A = A[ind]
num = 0
money = 0
for a, b in A:
    num += b
    if num < m:
        money += a * b
    else:
        money += a * (b - (num - m))
        break
print(money)
