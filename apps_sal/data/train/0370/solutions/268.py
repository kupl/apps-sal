
class DSU:

    def __init__(self):
        self.parent = defaultdict(lambda: -1)

    def union(self, x: int, y: int):
        xSet = self.find(x)
        ySet = self.find(y)
        self.parent[xSet] = ySet

    def find(self, x: int):
        if x not in self.parent:
            self.parent[x] = x
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]


class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        counts = Counter()
        dsu = DSU()
        for node in A:
            k = 2
            factors = []
            while k * k <= node:
                if node % k == 0:
                    factors.append(k)
                    while node % k == 0:
                        node //= k

                k += 1

            if node > 1:
                factors.append(node)

            for x, y in zip(factors, factors[1:]):
                dsu.union(x, y)

            if factors:
                counts[factors[0]] += 1

        finalCounts = Counter()

        for key in counts.keys():
            finalCounts[dsu.find(key)] += counts[key]

        return max(finalCounts.values())
