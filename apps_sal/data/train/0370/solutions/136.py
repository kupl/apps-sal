class UnionFind:
    def __init__(self, N):
        self.indices = list(range(N))

    def find(self, x):
        if x == self.indices[x]:
            return x

        self.indices[x] = self.find(self.indices[x])

        return self.indices[x]

    def union(self, x, y):
        x_i, y_i = self.find(x), self.find(y)

        self.indices[x_i] = y_i


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        n = len(A)
        UF = UnionFind(n)

        primes_set = defaultdict(list)

        def get_primes(num):
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    return get_primes(num // i) | set([i])
            return set([num])

        for i, num in enumerate(A):
            for factor in get_primes(num):
                primes_set[factor].append(i)

        for vals in primes_set.values():
            for i in range(len(vals) - 1):
                UF.union(vals[i], vals[i + 1])

        return max(Counter([UF.find(i) for i in range(n)]).values())
