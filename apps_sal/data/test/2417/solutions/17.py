import sys
import os
import math
import array
3


def main():
    N = read_int()
    A = read_ints()
    B = read_ints()
    print(solve(N, A, B))


def solve(N, A, B):
    T = {}
    i = 0
    for b in B:
        T[b] = i
        i += 1
    last_pos = -1
    ans = 0
    for a in A:
        t = T[a]
        if t > last_pos:
            last_pos = t
        else:
            ans += 1
    return ans


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
