#!/usr/bin/env python3
import sys
from itertools import chain
import numpy as np

# from itertools import combinations as comb
# form bisect import bisect_left, bisect_right, insort_left, insort_right
# from collections import Counter


def solve(N: int, A: "List[int]", B: "List[int]"):
    A = np.sort(A)
    B = np.sort(B)
    if N % 2 == 1:
        l = A[N // 2]
        r = B[N // 2]
        return r - l + 1
    else:
        l2 = A[N // 2 - 1] + A[N // 2]
        r2 = B[N // 2 - 1] + B[N // 2]
        return r2 - l2 + 1


def main():
    tokens = chain(*(line.split() for line in sys.stdin))
    # N, A, B = map(int, line.split())
    N = int(next(tokens))  # type: int
    AB = np.array(list(map(int, tokens)), dtype=np.int32)
    A = AB[0::2]
    B = AB[1::2]
    answer = solve(N, A, B)
    print(answer)


def __starting_point():
    main()


__starting_point()
