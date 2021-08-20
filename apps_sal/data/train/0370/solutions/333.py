class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        dsu = DSU()
        prime_to_index = {}
        for (i, num) in enumerate(A):
            primes = self.getPrimes(num)
            for prime in primes:
                if prime in prime_to_index:
                    dsu.union(prime_to_index[prime], i)
                else:
                    prime_to_index[prime] = i
        return max(dsu.count.values())

    def getPrimes(self, num):
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
            self.father[_a] = self.father[_b]
            self.count[_b] += self.count[_a]
