import numpy as np


def is_good(mid, key):
    x = A - mid // F
    return x[x > 0].sum() <= key


def binary_search(key):
    bad, good = -1, 10 ** 18
    while good - bad > 1:
        mid = (bad + good) // 2
        if is_good(mid, key):
            good = mid
        else:
            bad = mid
    return good


N, K = list(map(int, input().split()))
A = np.array(input().split(), dtype=np.int64)
F = np.array(input().split(), dtype=np.int64)
A.sort()
F[::-1].sort()
print((binary_search(K)))
