class UnionFind(object):
    def uf(self, n):
        self.uf = [i for i in range(n)]
        self.size = [1] * n

    def find(self, x):
        while x != self.uf[x]:
            self.uf[x] = self.uf[self.uf[x]]
            x = self.uf[x]
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
        def primeFactors(n):  # Prime factor decomposition
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

        idx_lookup = {A[i]: i for i in range(len(A))}  # in order to find idx in uf
        uf = UnionFind()
        uf.uf(len(A))
        primeAndItsMultiples = collections.defaultdict(list)  # {2: [4, 6], 3: [6, 15], 5: [15, 35], 7: [35]})

        for i in A:
            factors = primeFactors(i)
            for f in factors:
                primeAndItsMultiples[f].append(i)

        # we don't need to connect all the multiples of a prime,
        # just use the first multiple as their root
        for idx, multiples in primeAndItsMultiples.items():
            if multiples:
                root = multiples[0]  # use the first multiple as their root
                for node in multiples[1:]:
                    uf.union(idx_lookup[node], idx_lookup[root])  # connect node with root

        return max(uf.size)
