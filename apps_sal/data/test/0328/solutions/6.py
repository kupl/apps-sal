import sys
import math
3
DEBUG = False


def inp():
    return sys.stdin.readline().rstrip()


def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)


def main():
    N = int(inp())
    ans = 0
    for _ in range(N):
        (x, y) = [int(e) for e in inp().split()]
        ans = max(ans, x + y)
    print(ans)


def __starting_point():
    main()


__starting_point()
