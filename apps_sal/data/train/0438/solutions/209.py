from collections import Counter


class Union:
    def __init__(self, n):
        self.groups = list(range(n))
        self.sizes = [1] * n

    def find(self, node):
        while node != self.groups[node]:
            node = self.groups[node]
        return node

    def union(self, node1, node2):
        root1, root2 = self.find(node1), self.find(node2)
        if self.sizes[root1] < self.sizes[root2]:
            root1, root2 = root2, root1
        self.sizes[root1] += self.sizes[root2]
        self.groups[root2] = root1
        return self.sizes[root1]

    def getSize(self, node):
        node = self.find(node)
        return self.sizes[node]


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        union = Union(n)
        bits = [0] * n
        counter = Counter()
        res = -1
        for i, x in enumerate(arr):
            curr_size = 1
            x -= 1
            bits[x] = 1
            if x and bits[x - 1] == 1:
                l_size = union.getSize(x - 1)
                counter[l_size] -= 1
                curr_size = union.union(x - 1, x)

            if x < n - 1 and bits[x + 1] == 1:
                r_size = union.getSize(x + 1)
                counter[r_size] -= 1
                curr_size = union.union(x, x + 1)

            counter[curr_size] += 1
            if counter[m] > 0:
                res = i + 1
        return res
