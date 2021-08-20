class Solution:

    def largestComponentSize(self, A: List[int]) -> int:

        def prime_factors(n):
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return prime_factors(n // i) | set([i])
            return set([n])
        f = list(range(len(A)))

        def find(x):
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            f[find(x)] = find(y)
        p2i = dict()
        for (i, a) in enumerate(A):
            primes = prime_factors(a)
            for p in primes:
                if p in p2i:
                    union(i, p2i[p])
                else:
                    p2i[p] = find(i)
        counts = Counter(map(find, range(len(A))))
        return counts.most_common(1)[0][1]
