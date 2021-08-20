from collections import defaultdict, deque, Counter, OrderedDict
from bisect import bisect_left, bisect_right
from functools import reduce, lru_cache
from heapq import heappush, heappop, heapify
import itertools
import math
import fractions
import sys
import copy


def L():
    return sys.stdin.readline().split()


def I():
    return int(sys.stdin.readline().rstrip())


def SL():
    return list(sys.stdin.readline().rstrip())


def LI():
    return [int(x) for x in sys.stdin.readline().split()]


def LI1():
    return [int(x) - 1 for x in sys.stdin.readline().split()]


def LS():
    return [list(x) for x in sys.stdin.readline().split()]


def R(n):
    return [sys.stdin.readline().strip() for _ in range(n)]


def LR(n):
    return [L() for _ in range(n)]


def IR(n):
    return [I() for _ in range(n)]


def LIR(n):
    return [LI() for _ in range(n)]


def LIR1(n):
    return [LI1() for _ in range(n)]


def SR(n):
    return [SL() for _ in range(n)]


def LSR(n):
    return [LS() for _ in range(n)]


def perm(n, r):
    return math.factorial(n) // math.factorial(r)


def comb(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))


def make_list(n, *args, default=0):
    return [make_list(*args, default=default) for _ in range(n)] if len(args) > 0 else [default for _ in range(n)]


dire = [[1, 0], [0, 1], [-1, 0], [0, -1]]
dire8 = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
alphabets = 'abcdefghijklmnopqrstuvwxyz'
ALPHABETS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
MOD = 1000000007
INF = float('inf')
sys.setrecursionlimit(1000000)


class DoubleRollingHash:

    def __init__(self, seq, f=ord):
        self.n = len(seq)
        (self.base1, self.base2) = (1007, 2009)
        (self.mod1, self.mod2) = (1000000007, 1000000009)
        self.f = f
        (self.hash1, self.hash2) = ([0] * (self.n + 1), [0] * (self.n + 1))
        (self.power1, self.power2) = ([1] * (self.n + 1), [1] * (self.n + 1))
        for (i, e) in enumerate(seq):
            self.hash1[i + 1] = (self.hash1[i] * self.base1 + self.f(e)) % self.mod1
            self.hash2[i + 1] = (self.hash2[i] * self.base2 + self.f(e)) % self.mod2
            self.power1[i + 1] = self.power1[i] * self.base1 % self.mod1
            self.power2[i + 1] = self.power2[i] * self.base2 % self.mod2

    def get(self, l, r):
        v1 = (self.hash1[r] - self.hash1[l] * self.power1[r - l]) % self.mod1
        v2 = (self.hash2[r] - self.hash2[l] * self.power2[r - l]) % self.mod2
        return (v1, v2)

    def getLCP(self, a, b):
        l = self.n - max(a, b) + 1
        (left, right) = (0, l)
        while right - left > 1:
            mid = (left + right) // 2
            if self.get(a, a + mid) == self.get(b, b + mid):
                left = mid
            else:
                right = mid
        return left


class RollingHash:

    def __init__(self, seq, f=ord):
        self.n = len(seq)
        (self.base, self.mod) = (1007, pow(2, 61) - 1)
        self.f = f
        (self.hash, self.power) = ([0] * (self.n + 1), [1] * (self.n + 1))
        for (i, e) in enumerate(seq):
            self.hash[i + 1] = (self.hash[i] * self.base + self.f(e)) % self.mod
            self.power[i + 1] = self.power[i] * self.base % self.mod

    def get(self, l, r):
        return (self.hash[r] - self.hash[l] * self.power[r - l]) % self.mod

    def getLCP(self, a, b):
        l = self.n - max(a, b) + 1
        (left, right) = (0, l)
        while right - left > 1:
            mid = (left + right) // 2
            if self.get(a, a + mid) == self.get(b, b + mid):
                left = mid
            else:
                right = mid
        return left


def main():
    N = I()
    S = SL()
    rh = RollingHash(S)
    ans = 0

    def check(m):
        d = defaultdict(lambda: -1)
        for i in range(N - m + 1):
            v = rh.get(i, i + m)
            if d[v] != -1:
                if i >= d[v] + m:
                    return True
            else:
                d[v] = i
        return False
    (left, right) = (0, N // 2 + 1)
    while right - left > 1:
        mid = (left + right) // 2
        if check(mid):
            left = mid
        else:
            right = mid
    print(left)


def __starting_point():
    main()


__starting_point()
