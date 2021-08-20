class UnionFind:

    def __init__(self, n):
        self.reps = [i for i in range(n)]
        self.size = n

    def find(self, x):
        while x != self.reps[x]:
            self.reps[x] = self.reps[self.reps[x]]
            x = self.reps[x]
        return x

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        self.size -= 1
        self.reps[x] = y_root


class Solution:

    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        p2c = collections.defaultdict(set)
        c2p = collections.defaultdict(set)
        uf = UnionFind(n)
        for (i, (l, r)) in enumerate(zip(leftChild, rightChild)):
            if l != -1:
                p2c[i].add(l)
                c2p[l].add(i)
                uf.union(i, l)
                if i in p2c[l]:
                    return False
            if r != -1:
                p2c[i].add(r)
                c2p[r].add(i)
                uf.union(i, r)
                if i in p2c[r]:
                    return False
        for i in range(n):
            if len(c2p[i]) > 1:
                return False
        return uf.size == 1
