class DUSNode:
    def __init__(self, parent):
        self.parent = parent
        self.size = 0


class DisjointUnionSet:
    def __init__(self):
        self.forest = {}

    def addSet(self, node, key):
        self.forest[key] = node

    def find(self, p):
        while self.forest[p].parent != p:
            self.forest[p].parent = self.forest[self.forest[p].parent].parent
            p = self.forest[p].parent

        return p

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x != y:
            if self.forest[x].size < self.forest[y].size:
                x, y = y, x

            self.forest[y].parent = x
            self.forest[x].size += self.forest[y].size


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        composites = set()
        primes = []
        prime_factors = {k: v for k, v in zip(A, [[] for _ in range(len(A))])}
        maxA = max(A)
        for n in range(2, maxA + 1):
            if n not in composites:
                primes.append(n)
                m = n
                while m <= maxA:
                    composites.add(m)
                    if m in prime_factors:
                        prime_factors[m].append(n)

                    m += n

        djus = DisjointUnionSet()
        for p in primes:
            djus.addSet(DUSNode(p), p)

        for pf in list(prime_factors.values()):
            if pf:
                djus.forest[djus.find(pf[0])].size += 1

            for p1, p2 in zip(pf, pf[1:]):
                djus.union(p1, p2)

        return max([node.size for node in list(djus.forest.values())])
