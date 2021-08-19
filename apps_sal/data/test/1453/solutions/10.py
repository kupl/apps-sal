import sys
import os
3


def main():
    N, M = read_ints()
    A = read_ints()
    print(*solve(N, M, A))


def solve(N, M, A):
    A.sort()

    R = [0] * M
    s = 0
    ans = [0] * N
    for i, a in enumerate(A):
        s += a
        s += R[i % M]
        R[i % M] += a
        ans[i] = s

    return ans


###############################################################################

DEBUG = 'DEBUG' in os.environ


def inp():
    return sys.stdin.readline().rstrip()


def read_int():
    return int(inp())


def read_ints():
    return [int(e) for e in inp().split()]


def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)


def __starting_point():
    main()


__starting_point()
