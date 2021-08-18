class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        dsu = DSU(max(A))

        for n in A:
            for j in range(2, floor(sqrt(n)) + 1):
                if n % j == 0:
                    dsu.union(n, j)
                    dsu.union(n, n // j)

        maxSize = 0
        groupC = defaultdict(int)

        for n in A:
            parent = dsu.find(n)
            groupC[parent] += 1
            maxSize = max(maxSize, groupC[parent])

        return maxSize


class DSU:
    def __init__(self, largest):
        self.parent = [n for n in range(largest + 1)]
        self.sz = [1] * (largest + 1)

    def find(self, n):
        if n != self.parent[n]:
            self.parent[n] = self.find(self.parent[n])
        return self.parent[n]

    def union(self, n1, n2):
        xR, yR = self.find(n1), self.find(n2)

        if xR == yR:
            return

        if self.sz[xR] < self.sz[yR]:
            xR, yR = yR, xR

        self.parent[yR] = xR
        self.sz[yR] += self.sz[xR]

    def size(self, n):
        return self.sz[n]
