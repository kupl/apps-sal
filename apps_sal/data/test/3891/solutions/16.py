import sys
import math
3


def inp():
    return sys.stdin.readline().rstrip()


def solve(N, M, T):
    ax = -1
    ay = -1
    bx = -1
    by = -1
    for y in range(N):
        for x in range(M):
            if T[y][x] == 'B':
                if ax == -1:
                    ax = x
                    ay = y
                bx = x
                by = y
    return ((ay + by) // 2 + 1, (ax + bx) // 2 + 1)


def main():
    (N, M) = [int(e) for e in inp().split()]
    T = [inp() for _ in range(N)]
    print(*solve(N, M, T))


def __starting_point():
    main()


__starting_point()
