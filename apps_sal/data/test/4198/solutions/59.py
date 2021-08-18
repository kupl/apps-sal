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

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

stdin = sys.stdin


def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))
def ns(): return stdin.readline().rstrip()


A, B, X = na()


def judge(N, A, B, X):
    dn = len(str(N))
    if A * N + B * dn <= X:
        return True
    else:
        return False


def binary_search(A, B, X):
    left = 0
    right = 10 ** 9
    while right - left > 1:
        mid = left + (right - left) // 2
        if judge(mid, A, B, X):
            left = mid
        else:
            right = mid
    return left


if judge(10 ** 9, A, B, X):
    print(10 ** 9)
else:
    print(binary_search(A, B, X))
