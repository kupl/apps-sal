class FU:

    def __init__(self, n):
        self.p = [i for i in range(n)]

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        (px, py) = (self.find(x), self.find(y))
        self.p[py] = px


class Solution:

    def primeFactors(self, n):
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return self.primeFactors(n // i) | set([i])
        return set([n])

    def largestComponentSize(self, A: List[int]) -> int:
        fu = FU(len(A))
        primes = defaultdict(list)
        for i in range(len(A)):
            prime = self.primeFactors(A[i])
            for pr in prime:
                primes[pr].append(i)
        for (k, v) in list(primes.items()):
            for i in range(len(v) - 1):
                fu.union(v[i], v[i + 1])
        c = Counter([fu.find(i) for i in range(len(A))])
        return max(c.values())
