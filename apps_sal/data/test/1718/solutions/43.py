import sys
import bisect
import math
import itertools
import string
import queue
import copy
import heapq
import collections
import itertools
sys.setrecursionlimit(10 ** 8)
mod = 10 ** 9 + 7


def inp():
    return int(input())


def inpm():
    return map(int, input().split())


def inpl():
    return list(map(int, input().split()))


def inpls():
    return list(input().split())


def inplm(n):
    return list((int(input()) for _ in range(n)))


def inplL(n):
    return [list(input()) for _ in range(n)]


def inplT(n):
    return [tuple(input()) for _ in range(n)]


def inpll(n):
    return [list(map(int, input().split())) for _ in range(n)]


def inplt(n):
    return [tuple(map(int, input().split())) for _ in range(n)]


def inplls(n):
    return sorted([list(map(int, input().split())) for _ in range(n)])


(n, k) = inpm()
A = inpl()
print(math.ceil((n - 1) / (k - 1)))
