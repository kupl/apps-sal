class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        uf = UnionFind(n + 1, m)
        ans = -1
        visited = set()
        for i in range(n):
            a = arr[i]
            uf.add(a)
            if a - 1 in visited:
                uf.union(a, a - 1)
            if a + 1 in visited:
                uf.union(a, a + 1)
            if uf.cnt > 0:
                ans = i + 1
            visited.add(a)
        return ans


class UnionFind:
    def __init__(self, n, m):
        self.id = [-1 for _ in range(n)]
        self.size = [0 for _ in range(n)]
        self.cnt = 0
        self.m = m

    def add(self, i):
        self.id[i] = i
        self.size[i] = 1
        if self.get_size(i) == self.m:
            self.cnt += 1

    def find(self, i):
        root = i
        while root != self.id[root]:
            root = self.id[root]
        while root != i:
            j = self.id[i]
            self.id[i] = root
            i = j
        return root

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i == root_j:
            return
        if self.get_size(i) == self.m:
            self.cnt -= 1
        if self.get_size(j) == self.m:
            self.cnt -= 1
        if self.size[root_i] < self.size[root_j]:
            self.id[root_i] = root_j
            self.size[root_j] += self.size[root_i]
        else:
            self.id[root_j] = root_i
            self.size[root_i] += self.size[root_j]
        if self.get_size(root_i) == self.m:
            self.cnt += 1

    def get_size(self, i):
        return self.size[self.find(i)]
