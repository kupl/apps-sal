class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for i in range(n)]

    def GetParent(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.GetParent(self.parent[i])

        return self.parent[i]

    def Union(self, i, j):
        i_idx = self.GetParent(i)
        j_idx = self.GetParent(j)

        if j_idx == i_idx:
            return

        if self.rank[i_idx] > self.rank[j_idx]:
            self.parent[j_idx] = i_idx
        else:
            if self.rank[i_idx] == self.rank[j_idx]:
                self.rank[j_idx] += 1

            self.parent[i_idx] = j_idx


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        def prime_set(n):
            for i in range(2, math.floor(math.sqrt(n)) + 1):
                if n % i == 0:
                    return prime_set(n // i) | set([i])

            return set([n])

        ds = DisjointSet(len(A))

        primes = {}

        for i in range(len(A)):
            curr_prime_set = prime_set(A[i])

            for prime in curr_prime_set:
                primes.setdefault(prime, [])
                primes[prime].append(i)

        for key in primes:
            for i in range(len(primes[key]) - 1):
                ds.Union(primes[key][i], primes[key][i + 1])

        set_counter = {}

        for i in range(len(A)):
            set_counter.setdefault(ds.GetParent(i), 0)
            set_counter[ds.GetParent(i)] += 1

        return max(set_counter.values())
