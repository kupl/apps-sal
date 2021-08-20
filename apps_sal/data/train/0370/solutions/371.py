class UnionFind:

    def __init__(self, N):
        self.N = N
        self.rank = [1 for i in range(N)]
        self.parent = [i for i in range(N)]

    def find(self, x):
        y = x
        while x != self.parent[x]:
            x = self.parent[x]
        self.parent[y] = x
        return x

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        else:
            self.parent[py] = px
            if self.rank[px] == self.rank[py]:
                self.rank[px] += 1
        return True


class Solution:

    def largestComponentSize(self, A: List[int]) -> int:

        def union_all(x):
            for i in range(2, int(x ** 0.5) + 1):
                if x % i == 0:
                    uf.union(x, i)
                    uf.union(x, x // i)
        uf = UnionFind(100001)
        max_size = 1
        for i in range(len(A)):
            union_all(A[i])
        d = Counter()
        for i in range(len(A)):
            d[uf.find(A[i])] += 1
            max_size = max(max_size, d[uf.find(A[i])])
        return max_size
