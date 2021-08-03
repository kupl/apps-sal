import collections


class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size + 1)]
        self.rank = [0 for i in range(size + 1)]

    def find(self, num):
        if self.parent[num] != num:
            self.parent[num] = self.find(self.parent[num])
        return self.parent[num]

    def union(self, num1, num2):
        par1 = self.find(num1)
        par2 = self.find(num2)

        if par1 != par2:
            if self.rank[par1] > self.rank[par2]:
                self.parent[par2] = par1
            elif self.rank[par2] > self.rank[par1]:
                self.parent[par1] = par2
            else:
                self.parent[par2] = par1
                self.rank[par1] += 1


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        uf = UnionFind(max(A))
        a_to_factor = {}
        for a in A:
            factors = self.get_factors(a)
            a_to_factor[a] = factors[0]
            for i in range(len(factors) - 1):
                uf.union(factors[i], factors[i + 1])

        parent_to_count = collections.defaultdict(int)
        max_val = 0
        for a in A:
            parent = uf.find(a_to_factor[a])
            parent_to_count[parent] += 1
            max_val = max(max_val, parent_to_count[parent])
        return max_val

    def get_factors(self, num):
        i = 2
        factors = list()
        while i <= sqrt(num):
            if num % i == 0:
                factors.append(i)
                num = num // i
            else:
                i += 1

        factors.append(num)
        return list(set(factors))
