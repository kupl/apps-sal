class Union:
    def __init__(self, arr):
        self.weight = {}
        self.par = {}
        for a in range(1, max(arr) + 1):
            self.par[a] = a
            self.weight[a] = 1

    def find(self, a):
        while self.par[a] != a:
            a = self.par[a]
        return a

    def union(self, a, b):

        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return
        if self.weight[pa] < self.weight[pb]:
            pa, pb = pb, pa

        self.weight[pa] += self.weight[pb]
        self.par[pb] = pa

    def getMaxWeight(self):
        return max(list(map(len, list(self.weight.values()))))


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        union = Union(A)
        for a in A:
            sqr = int(sqrt(a))
            for j in range(2, sqr + 1):
                if a % j == 0:
                    union.union(a, a // j)
                    union.union(a, j)

        groups = collections.defaultdict(int)
        for a in A:
            groups[union.find(a)] += 1

        return max(groups.values())
