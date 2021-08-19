class DSU:

    def __init__(self, N):
        self.parent = list(range(N))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        self.parent[py] = px


class Solution:

    def largestComponentSize(self, A: List[int]) -> int:

        def primeSet(n):
            for i in range(2, int(sqrt(n)) + 1):
                if n % i == 0:
                    return primeSet(n // i) | {i}
            return {n}
        table = collections.defaultdict(list)
        for (i, num) in enumerate(A):
            primes = primeSet(num)
            for p in primes:
                table[p].append(i)
        N = len(A)
        dsu = DSU(N)
        for (_, indexes) in list(table.items()):
            for i in range(len(indexes) - 1):
                dsu.union(indexes[i], indexes[i + 1])
        return max(Counter([dsu.find(x) for x in range(N)]).values())
