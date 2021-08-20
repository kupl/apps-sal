class DSU:

    def __init__(self, arr):
        self.max_size = 0
        self.parent = [i for i in range(len(arr))]
        self.size = [1 for _ in range(len(arr))]

    def find(self, x):
        root = x
        while root != self.parent[root]:
            root = self.parent[root]
        while x != root:
            next_node = self.parent[x]
            self.parent[x] = root
            x = next_node
        return root

    def union(self, x, y):
        (r1, r2) = (self.find(x), self.find(y))
        if r1 == r2:
            return
        if self.size[r1] < self.size[r2]:
            self.size[r2] += self.size[r1]
            self.parent[r1] = r2
            self.max_size = max(self.max_size, self.size[r2])
        else:
            self.size[r1] += self.size[r2]
            self.parent[r2] = r1
            self.max_size = max(self.max_size, self.size[r1])


class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        primes = collections.defaultdict(list)

        def getPrimeFactors(n):
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
        prime_to_idx = {}
        dsu = DSU(A)
        for (i, n) in enumerate(A):
            primes = getPrimeFactors(n)
            for p in primes:
                if p in prime_to_idx:
                    dsu.union(i, prime_to_idx[p])
                prime_to_idx[p] = i
        return dsu.max_size
