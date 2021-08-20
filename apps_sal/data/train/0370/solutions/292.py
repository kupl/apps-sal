from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right
from functools import reduce, lru_cache
from typing import List
import itertools
import math
import heapq
import string
true = True
false = False
(MIN, MAX, MOD) = (-1061109567, 1061109567, 1000000007)


class UF:

    def __init__(self, n):
        self.p = list(range(n))
        self.size = [1] * n

    def merge(self, x, y):
        (px, py) = (self.find(x), self.find(y))
        if px == py:
            return
        if self.size[px] < self.size[py]:
            self.p[px] = py
            self.size[py] += self.size[px]
        else:
            self.p[py] = px
            self.size[px] += self.size[py]

    def find(self, x):
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]


class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        uf = UF(max(A) + 1)
        for n in A:
            for i in range(2, math.ceil(math.sqrt(n)) + 1):
                if n % i == 0:
                    uf.merge(n, i)
                    uf.merge(n, max(n // i, 2))
        return Counter(list(map(uf.find, A))).most_common()[0][1]


sol = Solution()
ns = [2, 3, 6, 7, 4, 12, 21, 39]
ns = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ns = [32, 5, 8, 11, 13, 78, 61, 16, 83, 22, 28, 93]
