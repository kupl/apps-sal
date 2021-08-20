from typing import List
from heapq import heappush, heappop, heapify


class Node:

    def __init__(self, parent, value):
        self.parent = parent
        self.rank = 0
        self.size = 1
        self.value = value


class UnionFind:

    def __init__(self, nodes):
        self.subsets = [Node(i, v) for (i, v) in enumerate(nodes)]
        self.maxSubsetSize = 1

    def union(self, i, j):
        irep = self.find(i)
        jrep = self.find(j)
        if irep == jrep:
            return
        if self.subsets[irep].rank > self.subsets[jrep].rank:
            self.subsets[jrep].parent = irep
            self.subsets[irep].size += self.subsets[jrep].size
        elif self.subsets[jrep].rank > self.subsets[irep].rank:
            self.subsets[irep].parent = jrep
            self.subsets[jrep].size += self.subsets[irep].size
        else:
            self.subsets[irep].parent = jrep
            self.subsets[jrep].rank += 1
            self.subsets[jrep].size += self.subsets[irep].size
        self.maxSubsetSize = max(self.maxSubsetSize, max(self.subsets[irep].size, self.subsets[jrep].size))

    def find(self, i):
        if self.subsets[i].parent != i:
            self.subsets[i].parent = self.find(self.subsets[i].parent)
        return self.subsets[i].parent


class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        uf = UnionFind(list(range(len(arr))))
        lengthMsets = set()
        last_step = -1
        if m == 1:
            lengthMsets.add(arr[0] - 1)
            last_step = 1
        numsets = set([arr[0] - 1])
        for i in range(1, len(arr), 1):
            num = arr[i] - 1
            numsets.add(num)
            if num - 1 in numsets:
                if uf.find(num - 1) in lengthMsets:
                    lengthMsets.remove(uf.find(num - 1))
                uf.union(num - 1, num)
            if num + 1 in numsets:
                if uf.find(num + 1) in lengthMsets:
                    lengthMsets.remove(uf.find(num + 1))
                uf.union(num + 1, num)
            if uf.subsets[uf.find(num)].size == m:
                lengthMsets.add(uf.find(num))
            if len(lengthMsets) > 0:
                last_step = i + 1
        return last_step
