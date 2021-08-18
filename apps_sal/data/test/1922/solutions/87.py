

import os
import sys


def main():
    N, M = list(map(int, input().split()))
    if N >= 2 and M >= 2:
        print(((N - 2) * (M - 2)))
    elif N < 2 and M >= 2:
        print((M - 2))
    elif N >= 2 and M < 2:
        print((N - 2))
    else:
        print((1))


def __starting_point():
    main()


__starting_point()
