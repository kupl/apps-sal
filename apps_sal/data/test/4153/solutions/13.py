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
sys.setrecursionlimit(10 ** 7)
inf = 10 ** 20
mod = 10 ** 9 + 7
stdin = sys.stdin


def ni():
    return int(ns())


def na():
    return list(map(int, stdin.readline().split()))


def ns():
    return stdin.readline().rstrip()


s = ns()
n = len(s)
b = s.count('0')
r = n - b
print(2 * min(b, r))
