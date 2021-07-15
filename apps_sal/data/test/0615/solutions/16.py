import numpy as np
N = int(input())
A = np.zeros(N+2, dtype=np.int64)
A[1:-1] = input().split()

np.cumsum(A, out = A)
total = A[-1]
A[-1] = 10 ** 18

left = np.searchsorted(A, A/2)
P1 = A[left-1]
P2 = A[left]
Q1,Q2 = A-P1, A-P2

np.maximum(P1,Q2,out = P1)
np.minimum(P2,Q1,out = P2)
P,Q = P1,P2

right = np.searchsorted(A,(total+A)/2)
R1 = A[right-1] - A
R2 = A[right] - A
S1 = total - A[right-1]
S2 = total - A[right]
np.maximum(R1,S2,out=R1)
np.minimum(R2,S1,out=R2)
R,S = R1,R2

PQRS = np.vstack([P,Q,R,S])
x = np.max(PQRS, axis=0) - np.min(PQRS, axis=0)
answer = (x[1:-1].min())
print(answer)
