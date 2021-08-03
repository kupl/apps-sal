class UnionFindSet:
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [1] * n

    def find(self, u):
        if u != self.parents[u]:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self.ranks[pu] > self.ranks[pv]:
            self.parents[pv] = pu
            self.ranks[pu] += self.ranks[pv]
        elif self.ranks[pu] < self.ranks[pv]:
            self.parents[pu] = pv
            self.ranks[pv] += self.ranks[pu]
        else:
            self.parents[pu] = pv
            self.ranks[pv] += self.ranks[pu]
        return True


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        def get_prime_factors(n):
            ans = set()
            while n % 2 == 0:
                ans.add(2)
                n //= 2
            for i in range(3, int(math.sqrt(n)) + 1, 2):
                while n % i == 0:
                    ans.add(i)
                    n //= i
            if n > 2:
                ans.add(n)
            return ans

        n = len(A)
        uf = UnionFindSet(n)

        dic = {}
        for i, a in enumerate(A):
            primes = get_prime_factors(a)
            for p in primes:
                if p in dic:
                    uf.union(i, dic[p])
                dic[p] = i

        return max(uf.ranks)
