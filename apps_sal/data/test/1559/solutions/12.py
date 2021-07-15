import os
import sys

import textwrap


def solve():
    L = int(input())
    A = input()

    size = len(A)
    div = int(size / L)
    mod = size % L

    if size == L:
        if A == '9'*L:
            print(str(10 ** (L - 1)) * (div + 1))
        else:
            print(int(A)+1)
    elif mod:
        print(str(10 ** (L - 1)) * (div + 1))
    else:
        parts = [int(x) for x in textwrap.wrap(A, L)]
        rep = parts[0]
        if rep == 10 ** L - 1:
            print(str(10 ** (L-1)) * (div+1))
        elif rep > parts[1]:
            print(str(rep) * div)
        elif rep < parts[1]:
            print(str(rep+1) * div)
        else:
            index = 2
            pl = len(parts)
            while index < pl and rep == parts[index]:
                index += 1
            if index == pl or parts[index] >= rep:
                print(str(rep + 1) * div)
            else:
                print(str(rep) * div)


def __starting_point():
    if "PYCHARM_HOSTED" in os.environ:
        sys.stdin = open('input.in')
    solve()

__starting_point()
