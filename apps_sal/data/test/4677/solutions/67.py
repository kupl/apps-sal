

import os
import sys


def main():
    S = input()
    stack = []
    for s in S:
        if s == '0' or s == '1':
            stack.append(s)
        elif s == 'B' and stack:
            stack.pop()
    for sta in stack:
        print(sta, end="")
    print()


def __starting_point():
    main()


__starting_point()
