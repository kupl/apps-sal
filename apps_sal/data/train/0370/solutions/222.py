class DSU:

    def __init__(self, n: int):
        self.n = n
        self.root = list(range(n))
        self.size = [1] * n
        self.max = 1

    def find(self, x: int) -> int:
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x: int, y: int):
        (rx, ry) = (self.find(x), self.find(y))
        if not rx == ry:
            self.root[rx] = ry
            self.size[ry] += self.size[rx]
            self.max = max(self.max, self.size[ry])


class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        n = len(A)
        dsu = DSU(n)
        seen = {}
        for (i, a) in enumerate(A):
            for j in range(2, int(math.sqrt(a)) + 1):
                if a % j:
                    continue
                if j in seen:
                    dsu.union(i, seen[j])
                else:
                    seen[j] = i
                if a // j in seen:
                    dsu.union(i, seen[a // j])
                else:
                    seen[a // j] = i
            if a in seen:
                dsu.union(i, seen[a])
            else:
                seen[a] = i
        return dsu.max
