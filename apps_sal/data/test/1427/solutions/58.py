from functools import reduce
from fractions import gcd
mod = 10**9 + 7
n, *A = map(int, open(0).read().split())
if len(A) == 1:
    print(1)
else:
    l = reduce(lambda x, y: x * y // gcd(x, y), A) % mod
    s = 0
    for a in A:
        s += l * pow(a, mod - 2, mod)
        s %= mod
    print(s)
