from collections import Counter
from operator import mul
from functools import reduce


def cmb(n, r):
    r = min(n - r, r)
    if r == 0:
        return 1
    over = reduce(mul, list(range(n, n - r, -1)))
    under = reduce(mul, list(range(1, r + 1)))
    return over // under


n = int(input())
al = list(map(int, input().split()))
c = Counter(al)
k = 0
for v in list(c.values()):
    if v == 1:
        continue
    else:
        k += cmb(v, 2)
for a in al:
    if c[a] == 1:
        print(k)
    elif c[a] == 2:
        print(k - cmb(c[a], 2))
    else:
        print(k - cmb(c[a], 2) + cmb(c[a] - 1, 2))
