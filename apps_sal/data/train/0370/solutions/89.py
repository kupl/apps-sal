class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return
        if self.rank[px] > self.rank[py]:
            self.parent[py] = px
            self.rank[px] += self.rank[py]
        else:
            self.parent[px] = py
            self.rank[py] += self.rank[px]


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        n = len(A)
        dsu = DSU(n)

        primes = defaultdict(list)
        for i, num in enumerate(A):
            pr_set = self.primes_set(num)
            for q in pr_set:
                primes[q].append(i)
        for _, indexes in list(primes.items()):
            for i in range(len(indexes) - 1):
                dsu.union(indexes[i], indexes[i + 1])

        # for i in range(n):
        #     for j in range(i+1,n):
        #         if A[i]!=A[j] and self.gcd(A[i],A[j]) > 1:
        #             dsu.union(i,j)
        return max(dsu.rank)

    def primes_set(self, n):
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return self.primes_set(n // i) | set([i])
        return set([n])

    def gcd(self, x, y):
        return gcd(y, x % y) if y != 0 else 0
