class UnionFind:

    def __init__(self, n, m):
        self.parents = {}
        self.size = {}
        self.rev_map = {}
        self.m = m
        for i in range(n):
            self.parents[i] = i
            self.size[i] = 0
            self.rev_map[i] = 0
        self.rev_map[i + 1] = 0
        self.rev_map[0] = 0

    def union(self, n1, n2):
        p1 = self.find_parent(n1)
        p2 = self.find_parent(n2)
        self.parents[p1] = p2
        self.rev_map[self.size[p1]] -= 1
        self.rev_map[self.size[p2]] -= 1
        self.size[p2] = self.size[p1] + self.size[p2]
        self.rev_map[self.size[p2]] += 1

    def find_parent(self, n1):
        if self.parents[n1] == n1:
            return n1
        self.parents[n1] = self.find_parent(self.parents[n1])
        return self.parents[n1]


class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        u = UnionFind(len(arr), m)
        d = [0] * max(arr)
        best = -1
        for i in range(len(arr)):
            d[arr[i] - 1] = 1
            u.size[u.find_parent(arr[i] - 1)] = 1
            u.rev_map[u.size[u.find_parent(arr[i] - 1)]] += 1
            if arr[i] - 2 >= 0 and d[arr[i] - 2] == 1:
                u.union(arr[i] - 2, arr[i] - 1)
            if arr[i] < len(arr) and d[arr[i]] == 1:
                u.union(arr[i] - 1, arr[i])
            if u.rev_map[m] >= 1:
                best = i
        if best == -1:
            return -1
        return best + 1
