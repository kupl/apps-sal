import numpy as np
from numba import njit

N = np.array([int(_) for _ in input()])


def solve(N):
    p, q = 0, 1
    for x in N:
        p, q = min(p + x, q + 10 - x), min(p + x + 1, q + 9 - x)
    print(p)


solve(N)
