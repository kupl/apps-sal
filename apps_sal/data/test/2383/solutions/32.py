#!/usr/bin/env python3
import sys
from itertools import chain


def solve(N: int, A: "List[int]"):
    cnt = 0
    for a in A:
        if a == cnt + 1:
            cnt += 1

    if cnt == 0:
        return -1
    return N - cnt


def main():
    tokens = chain(*(line.split() for line in sys.stdin))
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    answer = solve(N, A)
    print(answer)


def __starting_point():
    main()


__starting_point()
