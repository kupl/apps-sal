from decimal import ROUND_HALF_UP, Decimal  # 変換後の末尾桁を0や0.01で指定
from fractions import Fraction as frac  # frac(a,b)で正確なa/b
from itertools import combinations as com, permutations as per
from bisect import bisect_left as bileft, bisect_right as biright, insort
from functools import lru_cache
import sys
try:
    import os
    f = open('input.txt', 'r')
    sys.stdin = f
except FileNotFoundError:
    None
from math import sqrt, ceil, floor
from collections import deque, Counter, defaultdict
# defaultdict(int)
input = lambda: sys.stdin.readline().strip()
sys.setrecursionlimit(11451419)
#Decimal((str(0.5)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))
# @lru_cache(maxsize=10**10)
#######ここまでテンプレ#######
# ソート、"a"+"b"、再帰ならPython3の方がいい
#######ここから天ぷら########

n, m = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))


class UnionFind():
    def __init__(self, num):
        self.n = num
        self.parents = [{i} for i in range(self.n)]

    def find(self, x):
        if type(self.parents[x]) == set:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        xx = self.find(x)
        yy = self.find(y)
        if xx == yy:
            return
        else:
            size_xx = len(self.parents[xx])
            size_yy = len(self.parents[yy])
            if size_xx > size_yy:
                xx, yy = yy, xx

            # self.parents[yy]+=self.parents[xx]
            for t in self.parents[xx]:
                self.parents[yy].add(t)
            self.parents[xx] = yy

    def size(self, x):
        xx = self.find(x)
        return abs(self.parents[xx])

    def same(self, x, y):
        return 1 if self.find(x) == self.find(y) else 0

    def members(self, x):
        xx = self.find(x)
        return [i for i in range(self.n) if self.find(i) == xx]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def state_grouping(self):
        return list(self.all_group_members().values())


uf = UnionFind(n)
for i in range(m):
    a, b = list(map(int, input().split()))
    a -= 1; b -= 1
    uf.union(a, b)

# X= uf.state_grouping()
X = []
for l in uf.parents:
    if type(l) == set:
        X.append(l)

for l in X:
    ans = 0; ann = 0
    for i in l:
        ans += A[i]
        ann += B[i]
    if ans != ann:
        print("No"); return
else:
    print("Yes")
