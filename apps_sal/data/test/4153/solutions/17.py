

import os
import sys


def main():
    S = input()
    if S.count('0') < S.count('1'):
        print((S.count('0') * 2))
    else:
        print((S.count('1') * 2))


def __starting_point():
    main()


__starting_point()
