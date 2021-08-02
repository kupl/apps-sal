from numpy import *
N = int(input())
A = fromiter(map(int, input().split()), int64)
x = bitwise_xor.reduce(A)
A &= ~x
r = 0
while any(A):
    a = A.max()
    m = 1 << int(a).bit_length() - 1
    A[A & m > 0] ^= a
    r ^= a * (not r & m)
print(x + r + r)
