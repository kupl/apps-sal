from operator import mul
from functools import reduce


def cmb(n, r):
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


(N, M) = map(int, input().split())
if N <= 1:
    C = 0
else:
    C = cmb(N, 2)
if M <= 1:
    D = 0
else:
    D = cmb(M, 2)
print(C + D)
