from math import *


def bpow(a, n):
    res = 1
    while n > 0:
        if n % 2 != 0:
            res *= a
        a *= a
        n >>= 1
    return res


(M, N) = map(int, input().split())
sm = 0
for i in range(1, M):
    sm += bpow(i / M, N)
print(M - sm)
