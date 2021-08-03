import operator as op
from functools import reduce


def ncr(z, r):
    r = min(r, z - r)
    numer = reduce(op.mul, range(z, z - r, -1), 1)
    denom = reduce(op.mul, range(1, r + 1), 1)
    return numer // denom


n, m, k = list(map(int, input().strip().split()))
mod = 998244353
if m == 1:
    if k == 0:
        print(1)
    else:
        print(0)
elif n == 1:
    print(m)
else:
    ans = m * ((m - 1)**k)
    ans = ans % mod
    c = ncr(n - 1, k) % mod
    ans = ans * c
    ans = ans % mod
    print(ans)
