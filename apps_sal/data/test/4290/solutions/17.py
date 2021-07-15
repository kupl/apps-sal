from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if n <= 1: return 0
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

N, M = map(int, input().split())

print(cmb(N,2)+cmb(M,2))
