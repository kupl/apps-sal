import numpy as np


# 約数の列挙
def make_divisors(n):
    divisors = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return sorted(list(divisors))


N, K, *A = list(map(int, open(0).read().split()))

A = np.array(A, np.int64)
d = make_divisors(A.sum())

for i in d[::-1]:
    r = A % i
    r = r[r.nonzero()]
    l = r.size
    if l == 0:
        print(i)
        return
    else:
        n = np.arange(l - 1, 0, -1)
    r.sort()
    np.cumsum(r, out=r)
    if np.any((r[:-1] == i * n - (r[-1] - r[:-1])) & (r[:-1] <= K)):
        print(i)
        return

