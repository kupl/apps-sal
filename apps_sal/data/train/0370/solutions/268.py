# Build the graph by checking if every pair of nodes has a common factor greater than one, and if
# it does, connect them together (Create an edge between them). The only issue with this is that it
# runs in N^2 time.
#
# Then, we use dfs to find the largest connected component?
#
# Using dfs to find the largest connected component is okay, as it runs in N time, the problem is
# finding every edge for every pair of numbers in A takes too long (N^2 time).
#
# We can't use dfs as there are too many pairs to make. What needs to be done instead is to use
# union find to group nodes by factors.

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
