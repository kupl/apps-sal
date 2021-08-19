class UnionFind(object):

    def __init__(self, n):
        self.uf = [i for i in range(n)]
        self.size = [1] * n

    def find(self, x):
        while self.uf[self.uf[x]] != self.uf[x]:
            self.uf[x] = self.uf[self.uf[x]]
        return self.uf[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        self.uf[x_root] = y_root
        self.size[y_root] += self.size[x_root]
        self.size[x_root] = 0


class Solution:

    def largestComponentSize(self, A: List[int]) -> int:

        def factors(n):
            ff = set()
            while n % 2 == 0:
                ff.add(2)
                n //= 2
            for i in range(3, int(math.sqrt(n)) + 1, 2):
                while n % i == 0:
                    ff.add(i)
                    n //= i
            if n > 2:
                ff.add(n)
            return ff
        uf = UnionFind(len(A))
        pti = {}
        for (i, el) in enumerate(A):
            primes = factors(el)
            for p in primes:
                if p in pti:
                    uf.union(i, pti[p])
                pti[p] = i
        return max(uf.size)
