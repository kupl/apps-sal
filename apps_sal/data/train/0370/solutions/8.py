class DSU:
    def __init__(self, count):
        self.parent = [i for i in range(count)]
        self.size = [1 for _ in range(count)]
        self.max = 0

    def find(self, x):
        root = x
        while root != self.parent[root]:
            root = self.parent[root]
        while x != root:
            next_root = self.parent[x]
            self.parent[x] = root
            x = next_root
        return root

    def union(self, x, y):
        r1, r2 = self.find(x), self.find(y)
        if r1 == r2:
            return
        if self.size[r1] < self.size[r2]:
            self.size[r2] += self.size[r1]
            self.parent[r1] = r2
        else:
            self.size[r1] += self.size[r2]
            self.parent[r2] = r1
        self.max = max(self.max, self.size[r1], self.size[r2])


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        dsu = DSU(len(A))

        def getPrimeFactors(n):
            res = set()
            while n % 2 == 0:
                res.add(2)
                n //= 2
            for i in range(3, int(math.sqrt(n)) + 1, 2):
                while n % i == 0:
                    res.add(i)
                    n //= i
            if n > 2:
                res.add(n)
            return res
        prime_to_idx = {}
        for i, n in enumerate(A):
            primes = getPrimeFactors(n)
            for prime in primes:
                if prime in prime_to_idx:
                    dsu.union(i, prime_to_idx[prime])
                prime_to_idx[prime] = i
        return dsu.max
