import sys
import math
3


DEBUG = False


def inp():
    return sys.stdin.readline().rstrip()


def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)


def solve(N, M, K, B):
    segs = []
    for i in range(N - 1):
        segs.append(B[i + 1] - B[i])

    segs.sort()
    ntapes = N
    tapelen = N
    j = 0
    while ntapes > K:
        tapelen += segs[j] - 1
        ntapes -= 1
        j += 1

    return tapelen


def main():
    N, M, K = [int(e) for e in inp().split()]
    B = [int(e) for e in inp().split()]
    print(solve(N, M, K, B))


def __starting_point():
    main()


__starting_point()
