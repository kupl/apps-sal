class Solution:

    def largestComponentSize(self, A: List[int]) -> int:

        class UF:

            def __init__(self, N):
                self.parents = [i for i in range(N)]
                self.sizes = [1 for _ in range(N)]
                self.max = 1

            def find(self, x):
                if self.parents[x] != x:
                    self.parents[x] = self.find(self.parents[x])
                return self.parents[x]

            def union(self, x, y):
                x = self.find(x)
                y = self.find(y)
                if self.sizes[x] < self.sizes[y]:
                    (x, y) = (y, x)
                if x != y:
                    self.parents[y] = x
                    self.sizes[x] += self.sizes[y]
                    self.max = max(self.max, self.sizes[x])
        uf = UF(len(A))
        dic = {}
        for (i, num) in enumerate(A):
            for factor in range(2, int(math.sqrt(num) + 1)):
                if num % factor == 0:
                    for fac in [factor, num // factor]:
                        if fac in dic:
                            uf.union(dic[fac], i)
                        else:
                            dic[fac] = i
            if num in dic:
                uf.union(dic[num], i)
            else:
                dic[num] = i
        return uf.max
