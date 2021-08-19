#!/usr/bin/env python3
from itertools import product
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(
        X: int, Y: int, Z: int, K: int,
        A: "List[int]", B: "List[int]", C: "List[int]"):
    z = [0]

    def f(a: "List[int]"):
        nonlocal z
        a.sort(reverse=True)
        z = [zi + ai for zi, ai in product(z, a[:K])]
        z.sort(reverse=True)
        z = z[:K]

    f(A)
    f(B)
    f(C)
    for zi in z:
        print(zi)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    Z = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(X)]  # type: "List[int]"
    B = [int(next(tokens)) for _ in range(Y)]  # type: "List[int]"
    C = [int(next(tokens)) for _ in range(Z)]  # type: "List[int]"
    solve(X, Y, Z, K, A, B, C)


def __starting_point():
    main()


__starting_point()
