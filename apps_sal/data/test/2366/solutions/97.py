from functools import reduce
from operator import mul
import collections
N = int(input())
A = list(map(int, input().split()))
a = collections.Counter(A)


def combinations_count(n, r):
    r = min(r, n - r)
    numer = reduce(mul, range(n, n - r, -1), 1)
    denom = reduce(mul, range(1, r + 1), 1)
    return numer // denom


ans = 0
for i in a:
    if a[i] > 1:
        ans += combinations_count(a[i], 2)
for i in A:
    n = a[i]
    if n > 2:
        print(ans + combinations_count(n - 1, 2) - combinations_count(n, 2))
    elif n == 2:
        print(ans - 1)
    else:
        print(ans)
