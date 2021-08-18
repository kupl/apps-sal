import numpy as np


# 約数の列挙
def make_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

    divisors.sort()
    return divisors


N, K, *A = map(int, open(0).read().split())

A = np.array(A, np.int64)
d = make_divisors(A.sum())

for i in d[::-1]:
    r = A % i
    r.sort()
    r = r[r != 0]
    if r.size == 0:
        print(i)
        return
    else:
        n = np.arange(r.size - 1, 0, -1)

    np.cumsum(r, out=r)
    equal = np.where(r[:-1] == i * n - (r[-1] - r[:-1]))[0]
    if np.any(r[equal] <= K):
        print(i)
        return
