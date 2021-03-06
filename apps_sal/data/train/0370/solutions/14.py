class UF(object):

    def uf(self, n):
        self.uf = [i for i in range(n)]
        self.size = [1] * n

    def find(self, x):
        if x != self.uf[x]:
            self.uf[x] = self.find(self.uf[x])
        return self.uf[x]

    def union(self, x, y):
        xx = self.find(x)
        yy = self.find(y)
        if xx == yy:
            return
        self.uf[xx] = yy
        self.size[yy] += self.size[xx]


class Solution:

    def largestComponentSize(self, A: List[int]) -> int:

        def primefactors(n):
            out = set()
            while n % 2 == 0:
                out.add(2)
                n //= 2
            for i in range(3, int(math.sqrt(n)) + 1, 2):
                while n % i == 0:
                    out.add(i)
                    n //= i
            if n > 2:
                out.add(n)
            return out
        '\n        idx_lookup = {A[i] : i for i in range(len(A))} \n        uf = UF()\n        uf.uf(len(A))\n        # 使用因子作为key 来收集index表示公有相同因子\n        primeAndItsMultiples = collections.defaultdict(list)\n        for i in A:\n            factors = primefactors(i)\n            for f in factors:\n                primeAndItsMultiples[f].append(i)\n        for idx, multiples in primeAndItsMultiples.items():\n            if multiples:\n                root = multiples[0] # use the first multiple as their root\n                for node in multiples[1:]:\n                    uf.union(idx_lookup[node], idx_lookup[root]) # connect node with root             \n        return max(uf.size)\n        '
        uf = UF()
        uf.uf(len(A))
        prime = {}
        for (i, v) in enumerate(A):
            factors = primefactors(v)
            for p in factors:
                if p in prime:
                    uf.union(i, prime[p])
                else:
                    prime[p] = i
        return max(uf.size)
