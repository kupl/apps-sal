class DSU:

    def __init__(self, count):
        self.parent = [i for i in range(count)]
        self.size = [1 for _ in range(count)]

    def find(self, x):
        root = x
        while root != self.parent[root]:
            root = self.parent[root]
        while x != root:
            next_node = self.parent[x]
            self.parent[x] = root
            x = next_node
        return root

    def union(self, x, y):
        (r1, r2) = (self.find(x), self.find(y))
        if r1 == r2:
            return
        if self.size[r1] < self.size[r2]:
            self.size[r2] += self.size[r1]
            self.parent[r1] = r2
        else:
            self.size[r1] += self.size[r2]
            self.parent[r2] = r1

    def get_size(self, x):
        return self.size[self.find(x)]


class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        components = [0 for _ in range(len(arr))]
        ans = -1
        dsu = DSU(len(arr))
        size_count = collections.Counter()
        for (i, n) in enumerate(arr, 1):
            n -= 1
            components[n] = 1
            for adj in (n - 1, n + 1):
                if 0 <= adj < len(arr) and components[adj]:
                    size_count[dsu.get_size(adj)] -= 1
                    dsu.union(n, adj)
            size_count[dsu.get_size(n)] += 1
            if size_count[m] > 0:
                ans = i
        return ans
