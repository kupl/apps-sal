3

import math
import sys


DEBUG = False


def inp():
    return sys.stdin.readline().rstrip()


def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)


def solve(N, L, A, B):
    ans = 0

    last = 0
    for t, l in B:
        ans += (t - last) // A
        last = t + l

    ans += (L - last) // A

    return ans


def main():
    N, L, A = [int(e) for e in inp().split()]
    B = []
    for _ in range(N):
        t, l = [int(e) for e in inp().split()]
        B.append((t, l))

    print(solve(N, L, A, B))


def __starting_point():
    main()

__starting_point()
