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
    X = int(next(tokens))
    Y = int(next(tokens))
    Z = int(next(tokens))
    K = int(next(tokens))
    A = [int(next(tokens)) for _ in range(X)]
    B = [int(next(tokens)) for _ in range(Y)]
    C = [int(next(tokens)) for _ in range(Z)]
    solve(X, Y, Z, K, A, B, C)


def __starting_point():
    main()


__starting_point()
