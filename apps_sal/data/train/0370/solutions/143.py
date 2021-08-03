class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, target):
        if self.parent[target] != target:
            self.parent[target] = self.find(self.parent[target])
        return self.parent[target]

    def union(self, c, p):
        self.parent[self.find(c)] = self.find(p)


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        dsu = DSU(len(A))

        def prime_factorize(n):
            for i in range(2, int(sqrt(n)) + 1):
                if n % i == 0:
                    return [i] + prime_factorize(n // i)
            return [n]

        prime2indices = defaultdict(list)

        for i, n in enumerate(A):
            for p in prime_factorize(n):
                prime2indices[p].append(i)

        for arr in list(prime2indices.values()):
            for i in range(1, len(arr)):
                dsu.union(arr[0], arr[i])

        aggregate = defaultdict(int)

        for i in range(len(A)):
            aggregate[dsu.find(i)] += 1

        return max(aggregate.values())
