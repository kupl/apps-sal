class DSU:

    def __init__(self, count):
        self.components = count
        self.parent = [i for i in range(count)]
        self.size = [1 for _ in range(count)]

    def find(self, x):
        root = x
        while root != self.parent[root]:
            root = self.parent[root]
        while root != x:
            next_root = self.parent[x]
            self.parent[x] = root
            x = next_root
        return root

    def union(self, x, y):
        (r1, r2) = (self.find(x), self.find(y))
        if r1 == r2:
            return False
        if self.size[r1] < self.size[r2]:
            self.size[r2] += self.size[r1]
            self.parent[r1] = r2
        else:
            self.size[r1] += self.size[r2]
            self.parent[r2] = r1
        self.components -= 1
        return True


class Solution:

    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        dsu = DSU(n)
        for (i, left) in enumerate(leftChild):
            if left != -1:
                if not dsu.union(i, left):
                    return False
        for (i, right) in enumerate(rightChild):
            if right != -1:
                if not dsu.union(i, right):
                    return False
        return dsu.components == 1
