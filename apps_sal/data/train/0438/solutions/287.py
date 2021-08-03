class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def add(self, x):
        self.parent[x] = x
        self.rank[x] = 0

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xRoot, yRoot = self.find(x), self.find(y)

        if xRoot == yRoot:
            return

        xRank, yRank = self.rank[xRoot], self.rank[yRoot]
        if xRank < yRank:
            yRoot, xRoot = xRoot, yRoot

        self.parent[yRoot] = xRoot
        self.rank[xRoot] += self.rank[yRoot]
        # if self.rank[ yRoot] == self.rank[xRoot]:
        #     self.rank[xRoot] += 1

        return


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        if m == len(arr):
            return len(arr)
        if m > len(arr):
            return -1
        uf = UnionFind()

        for i in range(1, len(arr) + 1):
            uf.add(i)
        ans = -1
        seen = set()

        for i, n in enumerate(arr):
            uf.rank[n] = 1
            if n - 1 >= 1 and uf.rank[n - 1] != 0:
                if uf.rank[uf.find(n - 1)] == m:
                    ans = i
                uf.union(n, n - 1)
            if n + 1 <= len(arr) and uf.rank[n + 1] != 0:
                if uf.rank[uf.find(n + 1)] == m:
                    ans = i
                uf.union(n, n + 1)

        return ans
