from collections import defaultdict
import math
from collections import deque


class UnionFind:
    def __init__(self, n):
        self.parent = [-1] * n

    def find(self, a):
        if self.parent[a] < 0:
            return a
        self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            if self.parent[root_a] <= self.parent[root_b]:
                self.parent[root_a] += self.parent[root_b]
                self.parent[root_b] = root_a
            else:
                self.parent[root_b] += self.parent[root_a]
                self.parent[root_a] = root_b


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:

        def prime_factors(num):
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    return set([i]) | prime_factors(num // i)
            return set([num])

        uf = UnionFind(len(A))
        d = defaultdict(list)
        for i, a in enumerate(A):
            for p in prime_factors(a):
                d[p].append(i)

        for p, idx_list in list(d.items()):
            for i in range(len(idx_list) - 1):
                uf.union(idx_list[i], idx_list[i + 1])
        return -min(uf.parent)
