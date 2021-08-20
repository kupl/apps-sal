import sys
import math
3
DEBUG = False


def inp():
    return sys.stdin.readline().rstrip()


def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)


def solve(N):
    if N % 3 < 2:
        return (1, 1, N - 2)
    return (1, 2, N - 3)


def main():
    print(*solve(int(inp())))


def __starting_point():
    main()


__starting_point()
