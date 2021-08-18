import math
import itertools
import fractions
import heapq
import collections
import bisect
import sys
import queue
import copy

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 998244353
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()


class UnionFind():
    def __init__(self, sz):
        self.sz = sz
        self.data = [-1] * sz
        self.amount = [0] * sz

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        self.amount[x] += self.amount[y]
        self.amount[y] += self.amount[x]
        if self.data[x] > self.data[y]:
            x, y = y, x
        self.data[x] += self.data[y]
        self.data[y] = x
        return True

    def find(self, k):
        if self.data[k] < 0:
            return k
        self.data[k] = self.find(self.data[k])
        return self.data[k]

    def size(self, k):
        return -self.data[self.find(k)]

    def set_amount(self, k, k_amount):
        self.amount[k] = k_amount

    def get_amount(self, k):
        return self.amount[k]


def main():
    n, K = LI()
    field = [LI() for _ in range(n)]
    uf1 = UnionFind(n)
    uf2 = UnionFind(n)

    for i in range(n):
        l1 = [True] * n
        for j in range(i + 1, n):
            if not l1[i]:
                continue
            for k in range(n):
                if field[i][k] + field[j][k] > K:
                    l1[j] = False
                    break
        for j in range(i + 1, n):
            if l1[j]:
                uf1.unite(i, j)

    for i in range(n):
        l2 = [True] * n
        for j in range(i + 1, n):
            if not l2[i]:
                continue
            for k in range(n):
                if field[k][i] + field[k][j] > K:
                    l2[j] = False
                    break
        for j in range(i + 1, n):
            if l2[j]:
                uf2.unite(i, j)

    ans1 = 1
    check1 = [True] * n
    for i in range(n):
        sz = uf1.size(i)
        pa = uf1.find(i)
        if check1[pa]:
            check1[pa] = False
            _ans = 1
            for j in range(2, sz + 1):
                _ans *= j
                _ans %= mod
            ans1 *= _ans
            ans1 %= mod

    ans2 = 1
    check2 = [True] * n
    for i in range(n):
        sz = uf2.size(i)
        pa = uf2.find(i)
        if check2[pa]:
            check2[pa] = False
            _ans = 1
            for j in range(2, sz + 1):
                _ans *= j
                _ans %= mod
            ans2 *= _ans
            ans2 %= mod

    return (ans1 * ans2) % mod


print((main()))
