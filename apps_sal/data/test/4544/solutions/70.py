import numpy as np

N = int(input())
A = list(map(int, input().split()))
A = np.bincount(np.array(A, dtype='int64'))
Ans = A.copy()
Ans[1:] += A[:-1]
Ans[:-1] += A[1:]
print((max(Ans)))
