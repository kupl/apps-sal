class UF:

    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.size = [1 for i in range(N)]

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, X, Y):
        root_x = self.find(X)
        root_y = self.find(Y)
        if root_x != root_y:
            if self.size[root_x] >= self.size[root_y]:
                self.parent[root_y] = root_x
                self.size[root_x] += self.size[root_y]
            else:
                self.parent[root_x] = root_y
                self.size[root_y] += self.size[root_x]


class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        factor_map = {}
        uf = UF(len(A))
        for (index, num) in enumerate(A):
            for factor in range(2, int(sqrt(num) + 1)):
                if num % factor == 0:
                    if factor_map.get(factor) is None:
                        factor_map[factor] = index
                    else:
                        uf.union(index, factor_map[factor])
                    j = num // factor
                    if factor_map.get(j) is None:
                        factor_map[j] = index
                    else:
                        uf.union(index, factor_map[j])
            if factor_map.get(num) is None:
                factor_map[num] = index
            else:
                uf.union(index, factor_map[num])
        return max(uf.size)
