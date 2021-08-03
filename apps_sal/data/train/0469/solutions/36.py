class DSU:
    def __init__(self, n):
        self.p = [-1] * n
        self.r = [0] * n

    def find(self, x):
        if self.p[x] == -1:
            return x
        self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        r_x = self.find(x)
        r_y = self.find(y)
        if r_x == r_y:
            return False
        if self.r[r_x] > self.r[r_y]:
            self.p[r_y] = r_x
        else:
            self.p[r_x] = r_y
            if self.r[r_x] == self.r[r_y]:
                self.r[r_x] += 1
        return True


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        dsu = DSU(n)

        for i in range(n):
            if leftChild[i] != -1 and not dsu.union(i, leftChild[i]):
                return False
            if rightChild[i] != -1 and not dsu.union(i, rightChild[i]):
                return False

        return len([1 for i in range(n) if dsu.p[i] == -1]) == 1
