class UnionFind:

    def __init__(self, n):
        self.uf = list(range(n))
        self.size = defaultdict(lambda: 1)

    def find(self, i):
        if self.uf[i] != i:
            self.uf[i] = self.find(self.uf[i])
        return self.uf[i]

    def union(self, a, b):
        (x, y) = (self.find(a), self.find(b))
        if x == y:
            return
        self.uf[x] = self.uf[y]
        self.size[y] += self.size[x]
        del self.size[x]


def factors(n):
    if n % 2 == 0:
        yield 2
    while n % 2 == 0:
        n //= 2
    for i in range(3, int(n ** 0.5) + 2, 2):
        if i > n:
            break
        if n % i == 0:
            yield i
        while n % i == 0:
            n //= i
    if n > 2:
        yield n


class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        if not A:
            return 0
        u = UnionFind(len(A))
        x = {}
        for (i, a) in enumerate(A):
            for f in factors(a):
                if f in x:
                    u.union(i, x[f])
                else:
                    x[f] = i
        return max(u.size.values())
