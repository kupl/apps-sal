class UnionFind:

    def __init__(self, n):
        self.parents = list(range(n))
        self.count = n

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            self.count -= 1
            self.parents[px] = py


class Solution:

    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        uf = UnionFind(n)
        indegree = [0] * n
        for (parent, node) in enumerate(zip(leftChild, rightChild)):
            (l, r) = node
            if l != -1:
                indegree[l] += 1
                uf.union(l, parent)
            if r != -1:
                indegree[r] += 1
                uf.union(r, parent)
        return sum(indegree) == n - 1 and uf.count == 1
