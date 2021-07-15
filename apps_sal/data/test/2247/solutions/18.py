3

import math
import sys


DEBUG = False


def inp():
    return sys.stdin.readline().rstrip()


def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)


def solve(S, A, B, C):
    cnt = S // C
    cnt += B * (cnt // A)
    return cnt


def main():
    T = int(inp())
    for _ in range(T):
        S, A, B, C = [int(e) for e in inp().split()]
        print(solve(S, A, B, C))


def __starting_point():
    main()

__starting_point()
