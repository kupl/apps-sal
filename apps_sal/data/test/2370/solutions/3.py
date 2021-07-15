import sys
import numpy as np

read = sys.stdin.read

N, *A = list(map(int, read().split()))
A = np.array(A, np.int64).reshape(N, N)
'''
answer = 0
for i, j in product(range(N), repeat=2):
    if i < j:
        continue
    edge = A[i][j]
    for k in range(N):
        if i == k or j == k:
            continue

        tmp = A[i][k] + A[k][j]
        if tmp < edge:
            print(-1)
            return
        elif tmp == edge:
            break
    else:
        answer += edge
'''

useless = np.zeros_like(A)

for i in range(N):
    grid = A[i] + A[i, None].T
    if np.any(grid < A):
        print((-1))
        return
    grid[i] = np.inf
    grid[:, i] = np.inf

    useless |= (A == grid)

print((A[useless != 1].sum() // 2))

