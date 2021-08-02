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

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7


def LI(): return list(map(int, input().split()))
def II(): return int(input())
def LS(): return input().split()
def S(): return input()


def main():
    n = II()
    a = [int(c) for c in S()]
    b = [int(c) for c in S()]
    r1 = n
    a.sort()
    b.sort()
    bi = 0
    for c in a:
        while bi < n:
            if c <= b[bi]:
                bi += 1
                r1 -= 1
                break
            bi += 1

    bi = 0
    r2 = 0
    for c in a:
        while bi < n:
            if c < b[bi]:
                bi += 1
                r2 += 1
                break
            bi += 1
    return "{}\n{}".format(r1, r2)


print(main())
