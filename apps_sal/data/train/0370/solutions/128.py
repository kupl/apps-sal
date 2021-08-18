class Solution:
    def largestComponentSize(self, A: List[int]) -> int:

        def find_prime_factors(num):
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    return find_prime_factors(num // i) | set([i])
            return set([num])

        def find_root(x):
            if root[x] != x:
                root[x] = find_root(root[x])
            return root[x]

        def union(x, y):
            root[find_root(x)] = root[find_root(y)]

        root = [i for i in range(len(A))]
        prime_factor_to_index = defaultdict(list)
        for i, num in enumerate(A):
            prime_factors = find_prime_factors(num)
            for factor in prime_factors:
                prime_factor_to_index[factor].append(i)

        for indices in list(prime_factor_to_index.values()):
            for i in range(1, len(indices)):
                union(indices[i - 1], indices[i])

        root_count = Counter(find_root(i) for i in range(len(A)))
        return max(root_count.values())
