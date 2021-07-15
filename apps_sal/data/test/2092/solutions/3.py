3

import os
import sys


def main():
    M, N, K, T = read_ints()
    A = read_ints()
    B = [tuple(read_ints()) for _ in range(K)]
    print(solve(M, N, K, T, A, B))


def solve(M, N, K, T, A, B):
    B.sort()

    def seconds(agi):
        traps = [(l, r) for l, r, d in B if d > agi]
        x = 0
        sec = 0
        sw = -1
        for l, r in traps:
            if sw != -1 and sw < l:
                sec += 2 * (sw - x)
                sw = -1

            if sw != -1:
                sw = max(sw, r)
                continue

            sec += l - 1 - x
            x = l - 1
            sw = r

        if sw != -1:
            sec += 2 * (sw - x)

        sec += N + 1 - x
        return sec

    min_agi = min(A)
    max_agi = max(A)

    if seconds(max_agi) > T:
        return 0
    if seconds(min_agi) <= T:
        return len(A)

    lb = min_agi
    ub = max_agi
    while ub - lb > 1:
        agi = (lb + ub) // 2
        if seconds(agi) > T:
            lb = agi
        else:
            ub = agi

    return len([a for a in A if a >= ub])


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
