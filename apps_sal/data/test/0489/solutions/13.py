import operator as op
from functools import reduce


def comb(n, r):
    r = min(r, n - r)
    if r == 0:
        return 1
    numer = reduce(op.mul, range(n, n - r, -1))
    denom = reduce(op.mul, range(1, r + 1))
    return numer // denom


n = int(input())
l = [int(i)for i in input().split()]
d = sorted(l)
a = d[0]
b = d[1]
c = d[2]
if a == b and b == c:
    print(comb(l.count(a), 3))
elif a == b:
    print(l.count(c))
elif b == c:
    print(comb(l.count(c), 2))
else:
    print(l.count(c))
