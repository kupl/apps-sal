import numpy as np
import random

rand = False
if rand:
    N = 10 ** 5
    A = random.choices(list(range(1, 10**6)), k=N)
else:
    N = int(input())
    A = list(map(int, input().split()))

A.sort()
MX = max(A)
ret = np.zeros(MX + 1, dtype=np.bool)
A = np.array(A, dtype=np.int32)
ret[A] = True

for i in range(N - 1):
    m = A[i] * 2
    if A[i] == A[i + 1]: m = A[i]
    ret[np.arange(m, MX + 1, A[i])] = False

print((np.sum(ret)))
