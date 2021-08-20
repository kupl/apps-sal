def get_primes(max_num):
    return []


def get_prime_factors(num, primes):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return list(set(get_prime_factors(num // i, primes) + [i]))
    return [num]


class DisjointSet:

    def __init__(self, primes):
        self.primes = primes
        self.prime_parents = {}
        self.parent_to_count = {}

    def get_parent(self, prime):
        if prime not in self.prime_parents:
            self.prime_parents[prime] = -1
            return prime
        current = prime
        while self.prime_parents[current] > 0:
            current = self.prime_parents[current]
        return current

    def join(self, left, right):
        left_parent = self.get_parent(left)
        right_parent = self.get_parent(right)
        if left_parent == right_parent:
            return
        if self.prime_parents[left_parent] < self.prime_parents[right_parent]:
            larger = left_parent
            smaller = right_parent
        else:
            larger = right_parent
            smaller = left_parent
        self.prime_parents[larger] += self.prime_parents[smaller]
        self.parent_to_count[larger] = self.parent_to_count.get(larger, 0) + self.parent_to_count.get(smaller, 0)
        self.prime_parents[smaller] = larger

    def add(self, val):
        prime_factors = get_prime_factors(val, self.primes)
        for (l, r) in zip(prime_factors, prime_factors[1:]):
            self.join(l, r)
        parent = self.get_parent(prime_factors[0])
        self.parent_to_count[parent] = self.parent_to_count.get(parent, 0) + 1

    def get_largest_set_size(self):
        return max(self.parent_to_count.values())


class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        max_val = max(A)
        primes = get_primes(max_val)
        dj_set = DisjointSet(primes)
        for val in A:
            dj_set.add(val)
        return dj_set.get_largest_set_size()
