
import collections


class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size + 1)]
        self.rank = [1] * (size + 1)

    def find(self, num):
        if num != self.parent[num]:
            self.parent[num] = self.find(self.parent[num])

        return self.parent[num]

    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)

        if pa == pb:
            return

        if self.rank[pa] > self.rank[pb]:
            self.parent[pb] = pa
        elif self.rank[pb] > self.rank[pa]:
            self.parent[pa] = pb
        else:
            self.parent[pb] = pa
            self.rank[pa] += 1


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        uf = UnionFind(max(A))
        a_to_factor = {}
        for a in A:
            factors = self.find_factors(a)
            a_to_factor[a] = factors[0]
            for i in range(0, len(factors) - 1):
                uf.union(factors[i], factors[i + 1])

        parent_to_count = collections.defaultdict(int)
        max_num = 0
        for a in A:
            parent = uf.find(a_to_factor[a])
            parent_to_count[parent] += 1
            max_num = max(max_num, parent_to_count[parent])

        return max_num

    def find_factors(self, num):
        if num == 1:
            return [1]
        i = 2
        factors = list()
        while num >= i * i:
            if num % i == 0:
                factors.append(i)
                num = num // i
            else:
                i += 1
        factors.append(num)
        return list(set(factors))
