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
import copy
import functools

sys.setrecursionlimit(10**7)
inf = 10**20
gosa = 1.0 / 10**10
mod = 10**9 + 7


def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()


def main():
    n = I()
    a = n // 2
    b = n - a
    while fractions.gcd(a, b) > 1:
        a -= 1
        b += 1

    return "{} {}".format(a, b)


print(main())
