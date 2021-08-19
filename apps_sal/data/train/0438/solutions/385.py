from collections import defaultdict


class group:

    def __init__(self, n, m):
        self.groups = [i for i in range(n + 1)]
        self.group_size = {}
        self.m = m
        self.m_sizes = {}
        for i in range(1, n + 1):
            self.group_size[i] = 1

    def union(self, i, j):
        if i == j:
            self.group_size[i] = 1
            gi = gj = i
        else:
            gi = self.get_group(i)
            gj = self.get_group(j)
            if self.group_size[gi] > self.group_size[gj]:
                (gj, gi) = (gi, gj)
            self.groups[gi] = gj
        if self.group_size[gj] == self.m and gj in self.m_sizes:
            del self.m_sizes[gj]
        if self.group_size[gi] == self.m and gi in self.m_sizes:
            del self.m_sizes[gi]
        if i != j:
            self.group_size[gj] += self.group_size[gi]
        if self.group_size[gj] == self.m:
            self.m_sizes[gj] = 1
        return self.group_size[gj]

    def get_group(self, i):
        if self.groups[i] != i:
            self.groups[i] = self.get_group(self.groups[i])
        return self.groups[i]


class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        bits = [0] * (len(arr) + 2)
        GG = group(len(arr), m)
        steps = 0
        latest = -1
        for i in arr:
            steps += 1
            bits[i] = 1
            sz = 1
            if bits[i - 1] == 1:
                sz = GG.union(i - 1, i)
            if bits[i + 1] == 1:
                sz = GG.union(i, i + 1)
            if bits[i - 1] == bits[i + 1] == 0:
                sz = GG.union(i, i)
            if GG.m_sizes:
                latest = steps
        return latest
