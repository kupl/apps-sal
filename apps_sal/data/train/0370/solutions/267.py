class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        uf = UnionFind(max(A))
        for num in A:
            for factor in range(2, int(sqrt(num)) + 1):
                if num % factor == 0:
                    uf.union(num, factor)
                    uf.union(num, num // factor)
        res = 0
        group_count = collections.defaultdict(int)
        for num in A:
            group_id = uf.find(num)
            group_count[group_id] += 1
            res = max(res, group_count[group_id])
        return res

class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(0, size + 1)]
        self.size = [1] * (size + 1)
    
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)
        if parent_x == parent_y:
            return parent_x
        if self.size[parent_x] > self.size[parent_y]:
            parent_x, parent_y = parent_y, parent_x
        self.parent[parent_x] = parent_y
        self.size[parent_y] += self.size[parent_x]
        return parent_y

