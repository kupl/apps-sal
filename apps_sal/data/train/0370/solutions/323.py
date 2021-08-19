class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        factor = {}
        dsu = DSU()

        def get_primes(num):
            primes = set()
            i = 2
            while i * i <= num:
                if num % i == 0:
                    while num % i == 0:
                        num = num // i
                    primes.add(i)
                i += 1
            if num > 1:
                primes.add(num)
            return primes
        for num in A:
            primes = get_primes(num)
            for p in primes:
                factor.setdefault(p, num)
                if dsu.find(num) != dsu.find(factor[p]):
                    dsu.union(num, factor[p])
        ans = 0
        for v in list(factor.values()):
            ans = max(dsu.count[v], ans)
        return ans


class DSU:

    def __init__(self):
        self.father = {}
        self.count = {}

    def find(self, a):
        self.father.setdefault(a, a)
        self.count.setdefault(a, 1)
        if a != self.father[a]:
            self.father[a] = self.find(self.father[a])
        return self.father[a]

    def union(self, a, b):
        _a = self.find(a)
        _b = self.find(b)
        if _a != _b:
            self.father[_a] = _b
            self.count[_b] += self.count[_a]
