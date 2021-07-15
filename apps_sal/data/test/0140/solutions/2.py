3

import os
import sys


def main():
    N, M = read_ints()
    A = [tuple(read_ints()) for _ in range(N)]
    print(solve(N, M, A))


def solve(N, M, A):
    A.sort()

    D = {0: 0}
    for x, s in A:
        #dprint(x, s)
        #dprint(D)
        d = D.copy()
        for x0, c in d.items():
            if x - s <= x0 + 1:
                nx = x + s
                #dprint('  ', nx, '=>', c, '(x0=', x0, 'c=', c, ')')
                if nx not in D:
                    D[nx] = c
                else:
                    D[nx] = min(D[nx], c)
            else:
                nc = c + (x - s - x0 - 1)
                nx = x + s + nc - c
                #dprint('  ', nx, '=>', nc, '(x0=', x0, 'c=', c, ')')
                if nx not in D:
                    D[nx] = nc
                else:
                    D[nx] = min(D[nx], nc)
        #dprint(D)

    best = M * 2
    for x, c in D.items():
        if x == 0:
            continue
        if x < M:
            c += M - x
        best = min(best, c)
    return best


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
