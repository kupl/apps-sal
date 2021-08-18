import itertools
from collections import deque, defaultdict, Counter
from itertools import accumulate
import bisect
from heapq import heappop, heappush, heapify
import math
from copy import deepcopy
import queue
import numpy as np
Mod = 1000000007
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]
for i in range(2, 10**5 + 1):
    fact.append((fact[-1] * i) % Mod)
    inv.append((-inv[Mod % i] * (Mod // i)) % Mod)
    factinv.append((factinv[-1] * inv[-1]) % Mod)


def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % p


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


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n - k + 1):
        t = cmb(n - i - 1, k - 1, Mod)
        ans += (a[n - i - 1] * t % Mod - (a[i] * t % Mod)) % Mod

    print(ans % Mod)


def __starting_point():
    main()


__starting_point()
