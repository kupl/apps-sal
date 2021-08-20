from functools import reduce
from operator import mul
import collections
(n, a, b) = map(int, input().split())
al = list(map(int, input().split()))
newal = sorted(al, reverse=True)
ave = 0
ml = []
for i in range(a, b + 1):
    avet = sum(newal[:i]) / i
    if avet >= ave:
        ml.append(i)
        ave = max(ave, avet)
print(ave)
c = collections.Counter(al)


def cmb(n, r):
    r = min(n - r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


res = 0
for j in ml:
    r = c[newal[j - 1]]
    rr = newal.index(newal[j - 1])
    res += cmb(r, j - rr)
print(res)
