N = int(input())
import numpy as np
A = np.array([[int(x) for x in input().split()],[int(x) for x in input().split()]], dtype='int64')
A = A.cumsum(axis=1)
Ans = [A[0,i]+A[1,N-1]-A[1,i-1] if i > 0 else A[0,i]+A[1,N-1] for i in range(N)]
print(max(Ans))
