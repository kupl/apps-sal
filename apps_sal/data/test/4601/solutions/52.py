#!/usr/bin/env python3
import sys
from itertools import chain


def solve(N: int, K: int, H: "List[int]"):
    H = sorted(H, reverse=True)
    return sum(H[K:])


def main():
    tokens = chain(*(line.split() for line in sys.stdin))
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    H = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    answer = solve(N, K, H)
    print(answer)


def __starting_point():
    main()

__starting_point()
