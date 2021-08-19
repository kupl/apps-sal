class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        n = len(A)
        parents = [-1] * n
        factors = {}
        for (i, a) in enumerate(A):
            primes = self.primes(a)
            for p in primes:
                if p in factors:
                    self.union(parents, i, factors[p])
                factors[p] = i
        return max((-c for c in parents if c < 0))

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

    def find(self, parents, n):
        while parents[n] > 0:
            n = parents[n]
        return n

    def union(self, parents, i, j):
        (parent_i, parent_j) = (self.find(parents, i), self.find(parents, j))
        if parent_i != parent_j:
            if parents[parent_i] > parents[parent_j]:
                (parent_i, parent_j) = (parent_j, parent_i)
            parents[parent_i] += parents[parent_j]
            parents[parent_j] = parent_i
