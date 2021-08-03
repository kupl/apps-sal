""" 170/C
"""
import sys
import math
from functools import reduce
from bisect import bisect_left


def readString():
    return sys.stdin.readline()


def readInteger():
    return int(readString())


def readStringSet(n):
    return sys.stdin.readline().split(" ")[:n]


def readIntegerSet(n):
    return list(map(int, readStringSet(n)))


def readIntegerMatrix(n, m):
    return [lambda _: readIntegerSet(m) for _ in range(0, n)]


def main(X, N, P):
    mP = {}
    for p in P:
        mP[p] = p

    if X not in mP:
        return X

    i = 0
    while True:
        if X - i not in mP:
            return X - i

        if X + i not in mP:
            return X + i

        i += 1


def __starting_point():
    _X, _N = readIntegerSet(2)
    _P = readIntegerSet(_N)

    print(main(_X, _N, _P))


__starting_point()
