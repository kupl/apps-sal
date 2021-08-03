import sys
import math
3


DEBUG = False


def inp():
    return sys.stdin.readline().rstrip()


def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)


def getpf(E):
    if E == 0:
        return 0

    e = 0
    for k in range(2, E + 100):
        e += k - 1
        if e >= E:
            return k

    assert False


def solve(V, E):
    mx = V - getpf(E)
    mn = max(0, V - E * 2)
    return mn, mx


def main():
    N, M = [int(e) for e in inp().split()]
    print(*solve(N, M))


def __starting_point():
    main()


__starting_point()
