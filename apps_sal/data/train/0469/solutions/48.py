class Dsu:

    def __init__(self, n):
        self.p = [x for x in range(n)]
        self.r = [0 for x in range(n)]

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        (xx, yy) = (self.find(x), self.find(y))
        if xx == yy:
            return True
        if self.r[xx] > self.r[yy]:
            self.p[yy] = xx
        elif self.r[yy] > self.r[xx]:
            self.p[xx] = yy
        else:
            self.r[xx] += 1
            self.p[yy] = xx
        return False


class Solution:

    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        n = len(leftChild)
        x = 0
        y = 0
        z = 0
        f = [0 for i in range(n)]
        h = Dsu(n)
        for i in range(n):
            if leftChild[i] != -1:
                f[leftChild[i]] += 1
                h.union(i, leftChild[i])
            if rightChild[i] != -1:
                f[rightChild[i]] += 1
                h.union(i, rightChild[i])
        for (i, ii) in enumerate(f):
            if ii > 1:
                x += 1
            if h.find(i) == i:
                y += 1
            if ii == 0:
                z += 1
        if y != 1:
            return False
        elif z != 1:
            return False
        elif x > 0:
            return False
        else:
            return True
