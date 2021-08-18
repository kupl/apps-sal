import random

N = int(input())
A = list(map(int, input().split()))

S = A[0] + A[1]
X = 0
for a in A[2:]:
    X ^= a

D = (S - X) >> 1
if S != X + (D << 1) or D > A[0] or (X & D) != 0:
    print((-1))
    return

a = 0
b = 2**64
while b > 0:
    if (D & b) != 0:
        a |= b
    elif (X & b) != 0:
        if (a | b | D & (b - 1)) <= A[0]:
            a |= b
    b >>= 1
if a == 0:
    print((-1))
    return
print((A[0] - a))
