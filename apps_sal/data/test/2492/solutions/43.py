import numpy as np


def solve(*args: str) -> str:
    n, k = list(map(int, args[0].split()))
    A = np.array(sorted(map(int, args[1].split())))
    N = A[A < 0]
    P = A[0 < A]

    count = 0
    left, right = -10**18, 10**18
    while left + 1 < right:
        x = (left + right) // 2
        count = 0

        if k <= len(N) * len(P):
            count += (len(P) - np.searchsorted(P, -(-x // N), side='left')).sum()

        elif (n * (n - 1) - len(N) * (len(N) - 1) - len(P) * (len(P) - 1)) // 2 < k:
            for D in (-(N[::-1]), P):
                count += np.searchsorted(D, x // D, side='right').sum()
                count -= len(D[D * D <= x])
            count //= 2
            count += (n * (n - 1) - len(N) * (len(N) - 1) - len(P) * (len(P) - 1)) // 2

        else:
            right = 0
            break

        if count < k:
            left = x
        else:
            right = x

    return str(right)


def __starting_point():
    print((solve(*(open(0).read().splitlines()))))


__starting_point()
