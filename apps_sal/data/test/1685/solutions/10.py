import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect
import sys
import random
import time
sys.setrecursionlimit(10 ** 7)
inf = 10 ** 20
mod = 10 ** 9 + 7


def LI():
    return [int(x) for x in sys.stdin.readline().split()]


def LF():
    return [float(x) for x in sys.stdin.readline().split()]


def LS():
    return sys.stdin.readline().split()


def I():
    return int(sys.stdin.readline())


def F():
    return float(sys.stdin.readline())


def S():
    return input()


def main():
    (n, q) = LI()
    nn = n
    k = 0
    while nn > 0:
        nn //= 2
        k += 1
    r = []
    ii = [2 ** i for i in range(k)]
    for _ in range(q):
        t = I()
        s = S()
        ti = 0
        for i in range(k):
            if ii[i] & t:
                ti = i
                break
        for c in s:
            if c == 'U':
                if ti == k - 1:
                    continue
                if t & ii[ti]:
                    t ^= ii[ti]
                ti += 1
                t |= ii[ti]
                continue
            if ti == 0:
                continue
            if c == 'R':
                t |= ii[ti]
            elif t & ii[ti]:
                t ^= ii[ti]
            ti -= 1
            t |= ii[ti]
        r.append(t)
    return '\n'.join(map(str, r))


print(main())
