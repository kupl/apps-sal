import collections
import math

class UF:
    def __init__(self, N):
        self.parent = list(range(N))
        self.size = [1] * N
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            size_x, size_y = self.size[px], self.size[py]
            if size_x < size_y:
                self.parent[px] = py
                self.size[py] += size_x
            else:
                self.parent[py] = px
                self.size[px] += size_y

class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        factor_to_num_index = collections.defaultdict(int)
        uf = UF(len(A))
        for ind, num in enumerate(A):
            for factor in range(2, int(math.sqrt(num) + 1)):
                if num % factor == 0:
                    for fac in (factor, num // factor):
                        if fac in factor_to_num_index:
                            uf.union(ind, factor_to_num_index[fac])
                        else:
                            factor_to_num_index[fac] = ind
            if num not in factor_to_num_index:
                factor_to_num_index[num] = ind
            else:
                uf.union(ind, factor_to_num_index[num])
        return max(uf.size)


