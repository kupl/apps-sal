import re
import math
from collections import defaultdict
from collections import deque
import collections
from fractions import Fraction
import itertools
from copy import deepcopy
import random
import time
import os
import queue
import sys
import datetime
from functools import lru_cache
readline = sys.stdin.readline
sys.setrecursionlimit(2000000)
alphabet = 'abcdefghijklmnopqrstuvwxyz'
mod = int(10 ** 9 + 7)
inf = int(10 ** 20)


def yn(b):
    if b:
        print('yes')
    else:
        print('no')


def Yn(b):
    if b:
        print('Yes')
    else:
        print('No')


def YN(b):
    if b:
        print('YES')
    else:
        print('NO')


class union_find:

    def __init__(self, n):
        self.n = n
        self.P = [a for a in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if x != self.P[x]:
            self.P[x] = self.find(self.P[x])
        return self.P[x]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def link(self, x, y):
        if self.rank[x] < self.rank[y]:
            self.P[x] = y
        elif self.rank[y] < self.rank[x]:
            self.P[y] = x
        else:
            self.P[x] = y
            self.rank[y] += 1

    def unite(self, x, y):
        self.link(self.find(x), self.find(y))

    def size(self):
        S = set()
        for a in range(self.n):
            S.add(self.find(a))
        return len(S)


def ispow(a, b):
    now = b
    while now < a:
        now *= b
    if now == a:
        return True
    else:
        return False


def getbin(num, size):
    A = [0] * size
    for a in range(size):
        if num >> size - a - 1 & 1 == 1:
            A[a] = 1
        else:
            A[a] = 0
    return A


def getfacs(n, mod_=0):
    A = [1] * (n + 1)
    for a in range(2, len(A)):
        A[a] = A[a - 1] * a
        if mod_ > 0:
            A[a] %= mod_
    return A


def comb(n, r, mod, fac):
    if n - r < 0:
        return 0
    return fac[n] * pow(fac[n - r], mod - 2, mod) * pow(fac[r], mod - 2, mod) % mod


def nextcomb(num, size):
    x = num & -num
    y = num + x
    z = num & ~y
    z //= x
    z = z >> 1
    num = y | z
    if num >= 1 << size:
        return False
    else:
        return num


def getprimes(n, type='int'):
    if n == 0:
        if type == 'int':
            return []
        else:
            return [False]
    A = [True] * (n + 1)
    A[0] = False
    A[1] = False
    for a in range(2, n + 1):
        if A[a]:
            for b in range(a * 2, n + 1, a):
                A[b] = False
    if type == 'bool':
        return A
    B = []
    for a in range(n + 1):
        if A[a]:
            B.append(a)
    return B


def isprime(num):
    if num <= 1:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True


def ifelse(a, b, c):
    if a:
        return b
    else:
        return c


def join(A, c=''):
    n = len(A)
    A = list(map(str, A))
    s = ''
    for a in range(n):
        s += A[a]
        if a < n - 1:
            s += c
    return s


def factorize(n, type_='dict'):
    b = 2
    list_ = []
    while b * b <= n:
        while n % b == 0:
            n //= b
            list_.append(b)
        b += 1
    if n > 1:
        list_.append(n)
    if type_ == 'dict':
        dic = {}
        for a in list_:
            if a in dic:
                dic[a] += 1
            else:
                dic[a] = 1
        return dic
    elif type_ == 'list':
        return list_
    else:
        return None


def pm(x):
    return x // abs(x)


def inputintlist():
    return list(map(int, input().split()))


(H, W) = inputintlist()
ans = inf
for a in range(1, H):
    A = a * W
    B = (H - a) // 2 * W
    C = H * W - A - B
    ans = min(ans, max([A, B, C]) - min([A, B, C]))
    B = W // 2 * (H - a)
    C = H * W - A - B
    ans = min(ans, max([A, B, C]) - min([A, B, C]))
(H, W) = (W, H)
for a in range(1, H):
    A = a * W
    B = (H - a) // 2 * W
    C = H * W - A - B
    ans = min(ans, max([A, B, C]) - min([A, B, C]))
    B = W // 2 * (H - a)
    C = H * W - A - B
    ans = min(ans, max([A, B, C]) - min([A, B, C]))
print(ans)
