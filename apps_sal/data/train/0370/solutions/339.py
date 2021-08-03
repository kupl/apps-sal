class DSU:

    def __init__(self, N):
        self.data = list(range(N))

    def union(self, x, y):
        xp, yp = self.find(x), self.find(y)
        self.data[xp] = yp

    def find(self, x):
        if self.data[x] != x:
            self.data[x] = self.find(self.data[x])
        return self.data[x]


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:

        def primeFactors(n):

            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return primeFactors(n // i) | set([i])

            return set([n])

        primes = collections.defaultdict(list)

        for i, num in enumerate(A):
            factors = primeFactors(num)
            for factor in factors:
                primes[factor].append(i)

        dsu = DSU(len(A))

        for factor, nums in primes.items():
            for i in range(1, len(nums)):
                dsu.union(nums[i - 1], nums[i])

        counter = collections.Counter(dsu.find(i) for i in dsu.data)

        return max(v for v in counter.values())
