import numpy as np
s = int(input())
A = [0] * 2010
A[0] = 1
A[1] = A[2] = 0
for i in range(3, s + 1):
    for j in range(i - 2):
        A[i] += A[j]
        A[i] %= 7 + 10**9
print(A[s] % (7 + 10**9))
