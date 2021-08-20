import numpy as np
N = int(input())
A = np.array(list(map(int, input().split())), dtype=np.int64)
a = np.bitwise_xor.reduce(A)
for i in range(60):
    bit = 1 << i
    if bit & a:
        A ^= A & bit
for k in range(60, -1, -1):
    bit = 1 << k
    one = A & bit != 0
    i = np.where(one & (A < 1 << k + 1))[0]
    if len(i) == 0:
        continue
    i = i[0]
    x = A[i]
    A[one] ^= x
    A[i] = x
b = np.bitwise_xor.reduce(A)
a ^= b
print(a + b)
