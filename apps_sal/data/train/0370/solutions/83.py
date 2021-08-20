class Primes:

    def __init__(self, N):
        self.N = N
        self.primes = [0] * (N + 1)
        self.get_primes()

    def get_primes(self):
        for i in range(2, self.N + 1):
            if self.primes[i] == 0:
                self.primes[i] = i
                upto = self.N // i
                for j in range(2, upto + 1):
                    if self.primes[i * j] == 0:
                        self.primes[i * j] = i

    def __call__(self, n):
        if n <= 2:
            return {n}
        p = []
        while n >= 2:
            lp = self.primes[n]
            p.append(lp)
            n = n // lp
        return set(p)


class DisjointSet:

    def __init__(self, primes):
        self.primes = primes
        self.count = 1

    def union(self, setB):
        self.primes |= setB.primes
        self.count += setB.count


class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        disjoint_sets = []
        Factors = Primes(max(A))
        rank = [1] * (len(A) + 1)
        parent = [-1] * (len(A) + 1)
        m = dict()
        curr_count = 0

        def get_parent(x):
            if parent[x] == -1:
                return x
            parent[x] = get_parent(parent[x])
            return parent[x]

        def union(x, y):
            parx = get_parent(x)
            pary = get_parent(y)
            if parx == pary:
                return
            if rank[parx] >= rank[pary]:
                rank[parx] += rank[pary]
                parent[pary] = parx
            else:
                rank[pary] += rank[parx]
                parent[parx] = pary
        for (i, val) in enumerate(A):
            val_primes = Factors(val)
            for prime in val_primes:
                if prime in m:
                    union(m[prime], i)
                else:
                    m[prime] = i
        curr_count = max(rank)
        return curr_count
