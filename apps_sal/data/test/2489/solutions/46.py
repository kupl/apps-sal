#!/usr/bin/env python3
import sys
from itertools import chain
import numpy as np

# from itertools import combinations as comb
# form bisect import bisect_left, bisect_right, insort_left, insort_right
# from collections import Counter


def solve(N: int, A: "List[int]"):
    check = np.zeros(max(A) + 1, dtype=np.uint8)
    for ai in A:
        if check[ai] == 0:
            check[ai::ai] += 1
        else:
            check[ai] = 2

    answer = 0
    for ai in A:
        if check[ai] == 1:
            answer += 1

    return answer


def main():
    tokens = chain(*(line.split() for line in sys.stdin))
    # N, A = map(int, line.split())
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    answer = solve(N, A)
    print(answer)


def __starting_point():
    main()

__starting_point()
