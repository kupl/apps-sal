class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.number_of_groups = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_parent, y_parent = self.find(x), self.find(y)
        if x_parent == y_parent:
            return False
        if self.rank[x_parent] < self.rank[y_parent]:
            x_parent, y_parent = y_parent, x_parent

        self.rank[x_parent] += self.rank[y_parent]

        self.parent[y_parent] = x_parent

        self.number_of_groups -= 1
        return True


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        ans = -1
        uf = UnionFind(n)

        for i, x in enumerate(arr):
            x -= 1
            uf.rank[x] = 1
            for j in [x + 1, x - 1]:
                if 0 <= j < n:
                    if uf.rank[uf.find(j)] == m:
                        ans = i
                    if uf.rank[j]:
                        uf.union(x, j)

        if any(uf.rank[uf.find(i)] == m for i in range(n)):
            ans = n

        return ans
