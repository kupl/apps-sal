from collections import Counter
from collections import deque, defaultdict
import itertools as it
from math import gcd, floor, ceil, factorial
import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)


def inp():
    return int(input())


def inps():
    return input().rstrip()


def inpl():
    return list(map(int, input().split()))


def inpls():
    return list(map(str, input().split()))

# import decimal
# from decimal import Decimal
# decimal.getcontext().prec = 10


# from heapq import heappush, heappop, heapify
# import math


def lcd(a, b):
    return a * b // gcd(a, b)


def chmin(dp, i, x):
    if x < dp[i]: dp[i] = x; return True
    return False


def chmax(dp, i, x):
    if x > dp[i]: dp[i] = x; return True
    return False

# ---------------------------------------


class UnionFind:
    def __init__(self, num):
        self.parent = [i for i in range(num)]
        self.size = [1] * num

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        else:
            return x

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        else:
            if self.size[x] < self.size[y]:
                x, y = y, x
            self.parent[y] = x
            self.size[x] += 1

    def roots(self):
        st = set()
        for i in self.parent:
            st.add(i)
        return list(st)


N, M = inpl()
a = inpl()
b = inpl()
uf = UnionFind(N)
for i in range(M):
    c, d = inpl()
    c -= 1
    d -= 1
    uf.unite(c, d)

mp = dict()
for i in uf.roots():
    mp[i] = 0

for i in range(N):
    group = uf.find(i)
    mp[group] += a[i] - b[i]

bl = True
for k, v in list(mp.items()):
    if v != 0:
        bl = False
        break

print(("Yes" if bl else "No"))
