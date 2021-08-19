class UnionFind:

    def __init__(self, n):
        self.p = []
        self.size = [1] * n
        for i in range(n):
            self.p.append(i)
        self.max_union_size = 1

    def union(self, X, Y):
        (px, py) = (self.find(X), self.find(Y))
        if px == py:
            return
        elif self.size[px] < self.size[py]:
            self.p[px] = py
            self.size[py] += self.size[px]
            self.max_union_size = max(self.max_union_size, self.size[py])
        else:
            self.p[py] = px
            self.size[px] += self.size[py]
            self.max_union_size = max(self.max_union_size, self.size[px])

    def find(self, X):
        if self.p[X] != X:
            self.p[X] = self.find(self.p[X])
        return self.p[X]


class Solution:

    def largestComponentSize(self, A: List[int]) -> int:

        def get_prime_factors(num):
            n = num
            d = 2
            while d * d <= n:
                if n % d == 0:
                    yield d
                while n % d == 0:
                    n //= d
                d += 1
            if n > 1:
                yield n
        factors_to_nums = collections.defaultdict(list)
        for (i, a) in enumerate(A):
            for f in get_prime_factors(a):
                factors_to_nums[f].append(i)
        uf = UnionFind(len(A))
        for idx_of_num in factors_to_nums.values():
            for i in range(1, len(idx_of_num)):
                uf.union(idx_of_num[0], idx_of_num[i])
        return uf.max_union_size


' \n# lingnan 写的DisjointSet，还没有看\nclass DisjointSet:\n    def __init__(self, n):\n        self.parent = [-1] * n\n        self.max_size = 1\n    \n    \n    def find(self, x):\n        root = x\n        while self.parent[root] >= 0:\n            if self.parent[self.parent[root]] >= 0:\n                self.parent[root] = self.parent[self.parent[root]]\n            root = self.parent[root]\n        return root\n    \n    \n    def union(self, x, y):\n        x_root = self.find(x)\n        y_root = self.find(y)\n        \n        if x_root != y_root:\n            if self.parent[x_root] > self.parent[y_root]:\n                x_root, y_root = y_root, x_root\n            \n            self.parent[x_root] += self.parent[y_root]\n            self.parent[y_root] = x_root\n            self.max_size = max(self.max_size, -self.parent[x_root])\n    \n\nclass Solution:\n    def largestComponentSize(self, A: List[int]) -> int:\n        def get_prime_factors(num):\n            n = num\n            d = 2\n            while d * d <= n:\n                if n % d == 0:\n                    yield d\n                while n % d == 0:\n                    n //= d\n                d += 1\n            if n > 1:\n                yield n\n        \n        f_to_i = collections.defaultdict(list)\n        for i, a in enumerate(A):\n            for f in get_prime_factors(a):\n                f_to_i[f].append(i)\n        \n        ds = DisjointSet(len(A))\n        for indexes in f_to_i.values():\n            for i in range(1, len(indexes)):\n                ds.union(indexes[0], indexes[i])\n        \n        return ds.max_size\n'
