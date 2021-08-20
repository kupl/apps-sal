class UnionFindSet:

    def __init__(self, n):
        self.parants = [0] * n
        self.rank = [0] * n
        for i in range(n):
            self.parants[i] = i

    def find(self, x):
        if x != self.parants[x]:
            self.parants[x] = self.find(self.parants[x])
        return self.parants[x]

    def union(self, x, y):
        (px, py) = (self.find(x), self.find(y))
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            self.parants[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parants[py] = px
        else:
            self.parants[py] = px
            self.rank[py] += 1


class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        s = UnionFindSet(max(A) + 1)
        for x in A:
            for i in range(2, int(math.sqrt(x)) + 1):
                if x % i == 0:
                    s.union(x, i)
                    s.union(x, x // i)
        hash = defaultdict(int)
        for x in A:
            hash[s.find(x)] += 1
        return max(hash.values())
