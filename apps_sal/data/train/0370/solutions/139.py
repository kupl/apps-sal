class Solution:
    def largestComponentSize(self, A: List[int]) -> int:

        f = {}

        def find(x):
            f.setdefault(x, x)
            if x != f[x]:
                f[x] = find(f[x])

            return f[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                f[px] = py

        # we can break down any number into prime divisors mutiplication

        def get_primes(n):
            for i in range(2, int(sqrt(n)) + 1):
                if n % i == 0:
                    return get_primes(n // i) | {i}

            return {n}

        primes_dict = collections.defaultdict(list)

        for i, a in enumerate(A):
            primes = get_primes(a)

            for p in primes:
                primes_dict[p].append(i)

        for k, indexes in list(primes_dict.items()):
            for j in range(len(indexes) - 1):
                union(indexes[j], indexes[j + 1])

        return max(collections.Counter(find(i) for i in range(len(A))).values())
