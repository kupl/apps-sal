

import os
import sys


def main():
    N, M = list(map(int, input().split()))
    if N == 1 and M == 1:
        print((1))
    elif (N == 1 and M != 1):
        print((M - 2))
    elif (N != 1 and M == 1):
        print((N - 2))
    else:
        print(((N - 2) * (M - 2)))


def __starting_point():
    main()


__starting_point()
