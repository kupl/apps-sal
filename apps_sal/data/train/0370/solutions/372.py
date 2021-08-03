class UnionFind():
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        pi = self.find(i)
        pj = self.find(j)

        if pi != pj:
            self.parent[max(pi, pj)] = min(pi, pj)
            self.size[min(pi, pj)] += self.size[max(pi, pj)]


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        def decompose(num):
            if num == 1:
                return []
            res = []
            remain = num
            for factor in range(2, int(math.sqrt(num)) + 1):
                if remain % factor == 0:
                    while remain % factor == 0:
                        remain //= factor
                    res.append(factor)
            if remain > 1:
                res.append(remain)
            return res

        union_find = UnionFind(len(A))
        factor_index = dict()
        for idx, num in enumerate(A):
            factors = decompose(num)
            # print(\"factors\", factors)
            for factor in factors:
                if factor not in factor_index:
                    factor_index[factor] = idx
                else:
                    union_find.union(factor_index[factor], idx)
                # print(\"factor\", factor, \"unions\", unions.parent, unions.size )
        return max(union_find.size)
