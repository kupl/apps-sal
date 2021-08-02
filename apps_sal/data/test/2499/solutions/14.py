from numpy import *
f = bitwise_xor.reduce
N = int(input())
A = array(input().split(), int64)
X = f(A)
A = hstack((A, array([1 << i for i in range(60)if X & (1 << i)], int64)))
for k in range(60)[::-1]:
    b = 1 << k
    j = A & b != 0
    i = where(j & (A < 2 * b))[0]
    if len(i): i = i[0]; x = A[i]; A[j] ^= x; A[i] = x
r = f(A)
print(r + (r ^ X))
