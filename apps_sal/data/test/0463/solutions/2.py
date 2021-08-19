import sys
import os


def solve(a, x):
    occ = dict()
    for k in a:
        if k in occ:
            return 0
        else:
            occ[k] = True
    two = False
    occx = dict()
    for k in a:
        if k & x == k:
            continue
        elif k & x in occ:
            return 1
        elif k & x in occx:
            two = True
        else:
            occx[k & x] = True
    return 2 if two else -1


def main():
    (n, x) = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(a, x))


def __starting_point():
    main()


__starting_point()
