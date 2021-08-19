import math
from functools import lru_cache


@lru_cache(None)
def get_primes(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return get_primes(n // i) | set([i])
    return set([n])


class DSU:

    def __init__(self, n):
        self.store = list(range(n))

    def find(self, i):
        assert 0 <= i < len(self.store)
        if i != self.store[i]:
            self.store[i] = self.find(self.store[i])
        return self.store[i]

    def union(self, x, y):
        x_idx = self.find(x)
        y_idx = self.find(y)
        self.store[y_idx] = x_idx


class Solution:

    def largestComponentSize(self, a: List[int]) -> int:
        common_primes = defaultdict(list)
        for (i, num) in enumerate(a):
            for prime in get_primes(num):
                common_primes[prime].append(i)
        dsu = DSU(len(a))
        for idxs in list(common_primes.values()):
            for i in range(len(idxs) - 1):
                dsu.union(idxs[i], idxs[i + 1])
        return Counter((dsu.find(i) for i in range(len(a)))).most_common(1)[0][1]
