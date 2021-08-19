class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        if n == m:
            return n
        self.parent = list(range(n + 1))
        self.size = [0] * (n + 1)
        res = -1
        for (i, num) in enumerate(arr):
            if self.size[num] == 0:
                self.size[num] = 1
            if num - 1 >= 1 and self.size[num - 1] >= 1:
                if self.size[self.find(num - 1)] == m:
                    res = i
                self.union(num - 1, num)
            if num + 1 <= n and self.size[num + 1] >= 1:
                if self.size[self.find(num + 1)] == m:
                    res = i
                self.union(num, num + 1)
        return res

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.parent[root_a] = root_b
            self.size[root_b] += self.size[root_a]

    def find(self, a):
        curr = a
        while self.parent[curr] != curr:
            curr = self.parent[curr]
        (curr, root) = (a, curr)
        while self.parent[curr] != curr:
            (self.parent[curr], curr) = (root, self.parent[curr])
        return root
