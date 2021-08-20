import numpy as np


def solve(*args: str) -> str:
    (n, k) = list(map(int, args[0].split()))
    A = np.array(sorted(list(map(int, args[1].split()))))
    F = np.array(sorted(list(map(int, args[2].split())), reverse=True))
    right = 1 + A[-1] * F[0]
    left = -1
    total = A.sum()
    while left + 1 < right:
        mid = (left + right) // 2
        if total - np.minimum(A, mid // F).sum() <= k:
            right = mid
        else:
            left = mid
    return str(right)


def __starting_point():
    print(solve(*open(0).read().split('\n')))


__starting_point()
