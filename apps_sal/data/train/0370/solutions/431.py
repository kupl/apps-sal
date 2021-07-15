class DS:
    def __init__(self, N: int):
        self.p = list(range(N))
        self.size = [1] * N
        self.max = 1
    
    def find(self, node: int) -> int:
        if self.p[node] != node:
            self.p[node] = self.find(self.p[node])
        return self.p[node]
    
    def union(self, x: int, y: int) -> None:
        px, py = self.find(x), self.find(y)
        if px != py:
            sx, sy = self.size[px], self.size[py]
            if sx < sy:
                self.p[px] = py
                self.size[py] += sx
                self.max = max(self.max, self.size[py])
            else:
                self.p[py] = px
                self.size[px] += sy
                self.max = max(self.max, self.size[px])


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        factor_index = {}
        UF = DS(len(A))
        for idx, num in enumerate(A):
            for factor in range(2, int(num ** 0.5 + 1)):
                if num % factor == 0:
                    for fact in (factor, num // factor):
                        if fact in factor_index:
                            UF.union(factor_index[fact], idx)
                        else:
                            factor_index[fact] = idx
            if num in factor_index:
                UF.union(factor_index[num], idx)
            else:
                factor_index[num] = idx
        return UF.max

