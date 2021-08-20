from math import sqrt
from functools import reduce
from collections import defaultdict


class Disjoint:

    def __init__(self, N):
        self.parent = list(range(N))
        self.size = [1] * N

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, x, y):
        (px, py) = (self.find(x), self.find(y))
        if px != py:
            (sx, sy) = (self.size[px], self.size[py])
            if sx > sy:
                self.parent[py] = px
                self.size[px] += sy
            else:
                self.parent[px] = py
                self.size[py] += sx


class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        if not A:
            return 0
        fac_to_ind = defaultdict(int)
        un = Disjoint(len(A))
        for (ind, num) in enumerate(A):
            for fac in range(2, int(math.sqrt(num) + 1)):
                if num % fac:
                    continue
                for f in [fac, num // fac]:
                    if f not in fac_to_ind:
                        fac_to_ind[f] = ind
                    else:
                        un.union(ind, fac_to_ind[f])
            if num not in fac_to_ind:
                fac_to_ind[num] = ind
            else:
                un.union(ind, fac_to_ind[num])
        return max(un.size)
