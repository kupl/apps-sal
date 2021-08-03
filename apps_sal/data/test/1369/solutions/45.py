import numpy as np
from itertools import combinations

N = int(input())

P = [np.array(list(map(int, input().split())), dtype=float) for _ in range(N)]


def d2(v): return np.sum(np.square(v))


def radius(A, B, C):
    a = d2(B - C)
    b = d2(C - A)
    c = d2(A - B)

    r = float('inf')
    if c > d2(A + B - 2 * C):
        r = min(r, c)

    if a > d2(B + C - 2 * A):
        r = min(r, a)

    if b > d2(C + A - 2 * B):
        r = min(r, b)

    if r != float('inf'):
        return np.sqrt(r) / 2

    U = a * (b + c - a) * A + b * (c + a - b) * B + c * (a + b - c) * C
    v = a * (b + c - a) + b * (c + a - b) + c * (a + b - c)
    U /= v
    r = np.linalg.norm(U - A)
    return r


if N == 2:
    print((np.linalg.norm(P[0] - P[1]) / 2))
else:
    print((max(radius(a, b, c) for a, b, c in combinations(P, 3))))
