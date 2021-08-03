class DSU:
    def __init__(self, n):
        self.n = n
        self.fa = list(range(n))
        self.sz = [1 for _ in range(n)]

    def find(self, x):
        r = x
        while self.fa[r] != r:
            r = self.fa[r]
        i = x
        while i != r:
            i, self.fa[i] = self.fa[i], r
        return r

    def join(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            self.fa[x] = y
            self.sz[y] += self.sz[x]

    def size(self, x):
        x = self.find(x)
        return self.sz[x]


class Solution:
    def findLatestStep(self, a: List[int], m: int) -> int:
        n = len(a)
        b = [0 for _ in range(n)]
        dsu = DSU(n)

        ans = -1
        valid = set()
        for k, i in enumerate(a, 1):
            j = i - 1
            b[j] = 1
            if j > 0 and b[j - 1]:
                dsu.join(j, j - 1)
            if j + 1 < n and b[j + 1]:
                dsu.join(j, j + 1)

            if m == dsu.size(j):
                valid.add(j)

            valid = set(p for p in valid if m == dsu.size(p))
            if valid:
                ans = k

        return ans
