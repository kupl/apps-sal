max_num = 100000
smallest_prime_factors = [None] * (max_num + 1)
smallest_prime_factors[1] = 1

for num in range(2, max_num + 1):
    if smallest_prime_factors[num] is not None:
        continue
    smallest_prime_factors[num] = num
    for multiple in range(num * num, max_num + 1, num):
        if smallest_prime_factors[multiple] is None:
            smallest_prime_factors[multiple] = num


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        parents = {}

        def find(x):
            if x not in parents:
                parents[x] = x
            elif parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        def union(x, y):
            xx, yy = find(x), find(y)
            if xx != yy:
                parents[xx] = yy

        def decompose(num):
            if num == 1:
                return [1]
            prime_factor_set = set()
            while num != 1:
                prime_factor_set.add(smallest_prime_factors[num])
                num //= smallest_prime_factors[num]
            return list(prime_factor_set)

        factor = {}

        for num in A:
            prime_factors = decompose(num)
            factor[num] = prime_factors[0]
            for i in range(1, len(prime_factors)):
                union(prime_factors[i - 1], prime_factors[i])

        counts = Counter(find(factor[num]) for num in A)
        return max(counts.values() or [0])
