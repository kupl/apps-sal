import sys
from collections import deque
from bisect import bisect_left, bisect_right, insort_left, insort_right
from heapq import heapify, heappop, heappush
from itertools import product, permutations, combinations, combinations_with_replacement
from functools import reduce
from math import sin, cos, tan, asin, acos, atan

sys.setrecursionlimit(10**6)
INF = 10**20
eps = 1.0e-20
MOD = 10**9 + 7


def lcm(x, y):
    return x * y // gcd(x, y)


def lgcd(l):
    return reduce(gcd, l)


def llcm(l):
    return reduce(lcm, l)


def powmod(n, i, mod):
    return pow(n, mod - 1 + i, mod) if i < 0 else pow(n, i, mod)


def div2(x):
    return x.bit_length()


def div10(x):
    return len(str(x)) - (x == 0)


def perm(n, mod=None):
    ans = 1
    for i in range(1, n + 1):
        ans *= i
        if mod != None:
            ans %= mod
    return ans


def intput():
    return int(input())


def mint():
    return map(int, input().split())


def lint():
    return list(map(int, input().split()))


def ilint():
    return int(input()), list(map(int, input().split()))


def judge(x, l=['Yes', 'No']):
    print(l[0] if x else l[1])


def lprint(l, sep='\n'):
    for x in l:
        print(x, end=sep)


def ston(c, c0='a'):
    return ord(c) - ord(c0)


def ntos(x, c0='a'):
    return chr(x + ord(c0))


class counter(dict):
    def __init__(self, *args):
        super().__init__(args)

    def add(self, x):
        self.setdefault(x, 0)
        self[x] += 1


class comb():
    def __init__(self, n, mod=None):
        self.l = [1]
        self.n = n
        self.mod = mod

    def get(self, k):
        l, n, mod = self.l, self.n, self.mod
        k = n - k if k > n // 2 else k
        while len(l) <= k:
            i = len(l)
            l.append(l[i - 1] * (n + 1 - i) // i if mod == None else (l[i - 1] * (n + 1 - i) * powmod(i, -1, mod)) % mod)
        return l[k]


x = intput()
print(2 * (x // 11) + ((x % 11) != 0) + ((x % 11) > 6))
