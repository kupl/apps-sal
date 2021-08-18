

import os
import sys


def main():
    N = int(input())
    A = list(map(int, input().split()))
    i = N - 1

    if N % 2 == 1:
        while i < N:
            if i == N - 1:
                print("{}".format(A[i]), end='')
            else:
                print(" {}".format(A[i]), end='')
            if i == 0:
                i += 1
                continue
            if i % 2 == 0:
                i -= 2
            else:
                i += 2

    else:
        while i < N:
            if i == N - 1:
                print("{}".format(A[i]), end='')
            else:
                print(" {}".format(A[i]), end='')
            if i == 1:
                i -= 1
                continue
            if i % 2 == 0:
                i += 2
            else:
                i -= 2
    print()


def __starting_point():
    main()


__starting_point()
