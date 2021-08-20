import numpy as np
from itertools import combinations_with_replacement
import sys
read = sys.stdin.read
readlines = sys.stdin.readlines


def main():
    (n, m, q) = map(int, input().split())
    A = np.array(list(combinations_with_replacement(range(1, m + 1), n)))
    numA = len(A)
    score = np.zeros(numA, np.int32)
    ma = map(int, read().split())
    for (a, b, c, d) in zip(ma, ma, ma, ma):
        a -= 1
        b -= 1
        eachA_is_equalOrNot = A[:, b] - A[:, a] == c
        score += d * eachA_is_equalOrNot
    print(score.max())


def __starting_point():
    main()


__starting_point()
