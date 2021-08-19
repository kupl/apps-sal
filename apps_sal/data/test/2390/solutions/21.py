import sys
import itertools
from collections import deque, defaultdict, Counter
from itertools import accumulate
import bisect
from heapq import heappop, heappush
from fractions import gcd
from copy import deepcopy
import math
import queue
#import numpy as np
# import sympy as syp(素因数分解とか)
Mod = 1000000007

sys.setrecursionlimit(100000)


def sieve_of_eratosthenes(n):
    if not isinstance(n, int):
        raise TypeError("n is not int")
    if n < 2:
        raise ValueError("n is not effective")
    prime = [1] * (n + 1)
    for i in range(2, int(math.sqrt(n)) + 1):
        if prime[i] == 1:
            for j in range(2 * i, n + 1):
                if j % i == 0:
                    prime[j] = 0
    res = []
    for i in range(2, n + 1):
        if prime[i] == 1:
            res.append(i)
    return res


def factorial(i):
    if i == 1:
        return 1
    else:
        return i * factorial(i - 1)


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.rank = [0 for i in range(n + 1)]

    def findroot(self, x):
        if x == self.parent[x]:
            return x
        else:
            y = self.parent[x]
            y = self.findroot(self.parent[x])
            return y

    def union(self, x, y):
        px = self.findroot(x)
        py = self.findroot(y)
        if px < py:
            self.parent[py] = px
        else:
            self.parent[px] = py

    def same_group_or_no(self, x, y):
        return self.findroot(x) == self.findroot(y)


def main():  # startline--------------------------------------------
    n, c = list(map(int, input().split()))
    xv = [list(map(int, input().split())) for i in range(n)]
    x = [xv[i][0] for i in range(n)]
    v = [xv[i][1] for i in range(n)]
    r1, r2, l1, l2 = [0] * (n + 1), [0] * (n + 1), [0] * (n + 1), [0] * (n + 1)
    ans = 0
    dis = 0
    for i in range(n):
        r1[i + 1] = r1[i] + v[i] - (x[i] - dis)
        r2[i + 1] = r2[i] + v[i] - 2 * (x[i] - dis)
        dis = x[i]
    dis = c
    for i in reversed(list(range(n))):
        l1[n - i] = l1[n - i - 1] + v[i] - (dis - x[i])
        l2[n - i] = l2[n - i - 1] + v[i] - 2 * (dis - x[i])
        dis = x[i]
    for i in range(n):
        l1[i + 1] = max(l1[i + 1], l1[i])
        r1[i + 1] = max(r1[i + 1], r1[i])
    for i in range(n + 1):
        ans = max(ans, max(r2[i] + l1[n - i], l2[i] + r1[n - i]))
    print(ans)


def __starting_point():
    main()  # endline===============================================


__starting_point()
