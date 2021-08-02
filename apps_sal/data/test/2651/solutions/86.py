#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int


def solve(n: int, m: int, x: "List[int]", y: "List[int]"):
    X = 0
    for k in range(1, n + 1):
        X += (k - 1) * x[k - 1] - (n - k) * x[k - 1]
        X %= MOD
    Y = 0
    for k in range(1, m + 1):
        Y += (k - 1) * y[k - 1] - (m - k) * y[k - 1]
        Y %= MOD
    print((X * Y % MOD))

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    m = int(next(tokens))  # type: int
    x = [int(next(tokens)) for _ in range(n)]  # type: "List[int]"
    y = [int(next(tokens)) for _ in range(m)]  # type: "List[int]"
    solve(n, m, x, y)


def __starting_point():
    main()


__starting_point()
