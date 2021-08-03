class ds:
    def __init__(self, n):
        self.arr = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.arr[x] != x:
            self.arr[x] = self.find(self.arr[x])
        return self.arr[x]

    def union(self, x, y):
        Ax = self.find(x)
        Ay = self.find(y)
        if Ax == Ay:
            return False
        if self.size[Ax] > self.size[Ay]:
            Ax, Ay = Ay, Ax
        self.arr[Ax] = Ay
        self.size[Ay] += self.size[Ax]
        return True


def primes(n):
    odds = range(3, n + 1, 2)
    sieve = set(sum([list(range(q * q, n + 1, q + q)) for q in odds], []))
    return [2] + [p for p in odds if p not in sieve]


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        def factors(n):
            result = set()
            for p in primeNumber:
                while n % p == 0:
                    n //= p
                    result.add(p)
            if n > 1:
                result.add(n)
            return list(result)

        n, m = len(A), max(A)
        dsa = ds(m + 1)
        primeNumber = primes(round(m**.5) + 1)
        for d in A:
            rest = factors(d)
            for i in rest:
                dsa.union(d, i)
        return Counter([dsa.find(x) for x in A]).most_common(1)[0][1]
