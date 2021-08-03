import sys
import re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, atan2, degrees
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy, copy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd


def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return list(map(int, input().split()))
def LIST(): return list(map(int, input().split()))


sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7


def main():
    N = INT()
    li = LIST()
    A = defaultdict(int)
    for i in li:
        A[i] += 1
    cnt = 0
    for i in list(A.keys()):
        if i < A[i]:
            cnt += A[i] - i
        elif i > A[i]:
            cnt += A[i]

    print(cnt)


def __starting_point():
    main()


__starting_point()
