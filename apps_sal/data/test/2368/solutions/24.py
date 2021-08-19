import sys
import math
import random
import re
import heapq
from itertools import combinations as c, permutations as perm, product as p
from collections import deque
from copy import deepcopy
sys.setrecursionlimit(10**9)
INF = float('inf')
MOD = 10**9 + 7
#MOD = 998244353


def si(): return input()
def ii(): return int(input())
def fi(): return float(input())
def lstr(): return input().split()
def lint(): return list(map(int, input().split()))
def lintdec(): return list(map(lambda x: int(x) - 1, input().split()))
def lnstr(n): return [input() for _ in range(n)]
def lnint(n): return [ii() for _ in range(n)]
def lint_list(n): return [lint() for _ in range(n)]
def lcm(a, b): return a * b // math.gcd(a, b)


#######################################################
N, M = lint()


class UnionFind():
    def __init__(self):
        self.par = [0] * N
        self.rank = [0] * N
        for i in range(N):
            self.par[i] = i

    def root(self, x):
        if self.par[x] == x:
            return x
        parx = self.root(self.par[x])
        self.par[x] = parx
        return parx

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1


def main():
    UF = UnionFind()
    a = lint()
    b = lint()

    for _ in range(M):
        c, d = lintdec()
        UF.unite(c, d)

    roots = [UF.root(i) for i in range(N)]
    sum_a = {root: 0 for root in set(roots)}
    sum_b = sum_a.copy()

    for i in range(N):
        sum_a[roots[i]] += a[i]
        sum_b[roots[i]] += b[i]

    print('Yes' if sum_a == sum_b else 'No')


def __starting_point():
    main()


__starting_point()
