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
    return list(map(int, input().split()))


def II():
    return int(input())


def LS():
    return input().split()


def S():
    return input()


def main():
    n = II()
    a = LI()
    for i in range(0, n, 2):
        j = n - i - 1
        if j <= i:
            break
        (a[i], a[j]) = (a[j], a[i])
    return ' '.join(map(str, a))


print(main())
