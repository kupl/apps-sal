import numpy as np


def is_good(mid, key):
    return A_sum - np.minimum(A, mid // F).sum() <= key


def binary_search(bad, good, key):
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
A_sum = A.sum()
ans = binary_search(-1, np.max(A * F), K)
print(ans)

