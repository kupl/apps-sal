class Solution:
    def largestComponentSize(self, A: List[int]) -> int:

        uf = UnionFind(max(A))

        for a in A:
            for factor in range(2, int(sqrt(a)) + 1):
                if a % factor == 0:
                    uf.union(a, factor)
                    uf.union(a, a // factor)

        count_ = defaultdict(int)
        out = 0

#         print(uf.parent)
#         print(uf.size)

        for a in A:
            groupid = uf.find(a)
            count_[groupid] += 1
            out = max(out, count_[groupid])

        return out


class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size + 1)]
        self.size = [1] * (size + 1)

    def find(self, num):
        if self.parent[num] != num:
            self.parent[num] = self.find(self.parent[num])

        return self.parent[num]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)

        if self.size[px] > self.size[py]:
            px, py = py, px

        self.parent[px] = py
        self.size[py] += self.size[px]
