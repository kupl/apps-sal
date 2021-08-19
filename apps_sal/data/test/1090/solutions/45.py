import sys
from itertools import groupby


def input():
    return sys.stdin.readline().rstrip()


def main():
    (n, k) = map(int, input().split())
    S = list(input())
    p = len(list(groupby(S))) - 2 * k
    pp = max(p, 1)
    print(n - pp)


def __starting_point():
    main()


__starting_point()
