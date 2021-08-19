class DSU:

    def __init__(self, N):
        self.parent = list(range(N))
        self.size = [1] * N

    def find(self, x):
        root = x
        while root != self.parent[root]:
            root = self.parent[root]
        while x != root:
            temp = self.parent[x]
            self.parent[x] = root
            x = temp
        return root

    def union(self, x, y):
        root1 = self.find(x)
        root2 = self.find(y)
        if root1 == root2:
            return False
        if self.size[root1] > self.size[root2]:
            self.parent[root2] = root1
            self.size[root1] += self.size[root2]
        else:
            self.parent[root1] = root2
            self.size[root2] += self.size[root1]
        return True


class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        dsu = DSU(100001)
        for x in A:
            for j in range(2, int(x ** 0.5) + 1):
                if x % j == 0:
                    dsu.union(x, j)
                    dsu.union(x, x // j)
        counter = collections.Counter()
        max_val = 0
        for x in A:
            counter[dsu.find(x)] += 1
        return counter.most_common(1)[0][1]
