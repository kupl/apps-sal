import sys
import os
3


def main():
    K = read_ints()
    A = [read_ints(), read_ints(), read_ints()]
    print(solve(K, A))


def solve(K, A):
    N = sum(K)
    INF = N + 1
    loc = [-1] * N
    for i in range(3):
        for a in A[i]:
            loc[a - 1] = i
    D = [0, 0, 0]
    for i in loc:
        if i == 0:
            D = [D[0], min(D[0] + 1, D[1] + 1), min(D[0] + 1, D[1] + 1, D[2] + 1)]
        elif i == 1:
            D = [D[0] + 1, min(D[0], D[1]), min(D[0] + 1, D[1] + 1, D[2] + 1)]
        else:
            D = [D[0] + 1, min(D[0] + 1, D[1] + 1), min(D[0], D[1], D[2])]
    return min(D)


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
