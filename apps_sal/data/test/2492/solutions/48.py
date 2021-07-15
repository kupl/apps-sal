# coding: utf-8
import numpy as np


def solve(*args: str) -> str:
    n, k = list(map(int, args[0].split()))
    A = np.array(sorted(map(int, args[1].split())))
    N = A[A < 0]
    P = A[0 < A]

    count = 0
    left, right = -10**18, 10**18
    while left+1 < right:
        x = (left+right)//2
        count = (n-np.searchsorted(A, -(-x//N), side='left')).sum()
        count += n * (A == 0).sum() if 0 <= x else 0
        count += np.searchsorted(A, x//P, side='right').sum()
        count -= (A*A <= x).sum()
        count //= 2

        if count < k:
            left = x
        else:
            right = x

    return str(right)


def __starting_point():
    print((solve(*(open(0).read().splitlines()))))

__starting_point()
