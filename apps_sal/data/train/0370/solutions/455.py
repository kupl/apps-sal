class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        parents = [-1] * len(A)
        factors = {}
        for (i, a) in enumerate(A):
            primes = self.primes(a)
            for p in primes:
                factors.setdefault(p, i)
                self.union(parents, i, factors[p])
        return max((-c for c in parents))

    def primes(self, n):
        ans = set()
        while not n % 2:
            ans.add(2)
            n //= 2
        for i in range(3, int(sqrt(n)) + 1, 2):
            while not n % i:
                ans.add(i)
                n //= i
        if n > 1:
            ans.add(n)
        return ans

    def find(self, parents, x):
        while parents[x] > 0:
            x = parents[x]
        return x

    def union(self, parents, i, j):
        (parent_i, parent_j) = (self.find(parents, i), self.find(parents, j))
        if parent_i != parent_j:
            if parents[parent_i] > parents[parent_j]:
                (parent_i, parent_j) = (parent_j, parent_i)
            parents[parent_i] += parents[parent_j]
            parents[parent_j] = parent_i
