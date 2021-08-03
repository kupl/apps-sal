import itertools
from collections import deque, defaultdict, Counter
from itertools import accumulate
import bisect
from heapq import heappop, heappush, heapify
import math
from copy import deepcopy
import queue
import numpy as np
# sympy as syp(素因数分解とか)
Mod = 1000000007


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
            self.parent[y] = px
        else:
            self.parent[px] = py

    def same_group_or_no(self, x, y):
        return self.findroot(x) == self.findroot(y)


def main():  # startline-------------------------------------------
    def divisor(n):
        res = []
        for i in range(1, int(np.sqrt(n)) + 1):
            if n % i == 0:
                res.append(i)
                j = n // i
                if j != i:
                    res.append(j)
        res.sort(reverse=True)
        return res[::-1]
    n = int(input())
    div1 = divisor(n - 1)
    div2 = divisor(n)
    ans = len(div1) - 1
    for d in div2:
        if d == 1:
            continue
        nn = n
        while nn % d == 0:
            nn //= d
        if nn % d == 1:
            ans += 1

    print(ans)


def __starting_point():
    main()  # endline===============================================


__starting_point()
