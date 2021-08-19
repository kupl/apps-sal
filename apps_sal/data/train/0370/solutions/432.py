class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        if not A:
            return 0

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent_x, parent_y = find(x), find(y)
            if parent_x != parent_y:
                parent[parent_x] = parent_y

        primes = []
        for x in range(2, int(max(A)**0.5) + 1):
            for y in primes:
                if x % y == 0:
                    break  # break
            else:
                primes.append(x)

        factors = defaultdict(list)
        for a in A:
            x = a
            for p in primes:
                if p * p > x:
                    break  # break
                if x % p == 0:
                    factors[a].append(p)
                    while x % p == 0:
                        x //= p
            if x > 1:
                factors[a].append(x)
                primes.append(x)

        primes = list(set(primes))

        n = len(primes)
        primes_idx = {p: i for i, p in enumerate(primes)}

        parent = [i for i in range(n)]

        for a in A:
            if factors[a]:
                p0 = factors[a][0]
                for p in factors[a][1:]:
                    union(primes_idx[p0], primes_idx[p])

        count = Counter(
            find(primes_idx[factors[a][0]]) for a in A if factors[a])
        return max(count.values())
