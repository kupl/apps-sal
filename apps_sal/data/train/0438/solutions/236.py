class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        uf = UnionFind(n)
        res = [0] * n
        ans = -1
        for i in range(n):
            step = i + 1
            index = arr[i] - 1
            res[index] = 1
            uf.size[index] = 1
            uf.count[1] += 1

            if index - 1 >= 0 and res[index - 1] == 1:
                uf.union(index - 1, index)

            if index + 1 < n and res[index + 1] == 1:
                uf.union(index, index + 1)

            if uf.count[m] > 0:
                ans = step

        return ans


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [0] * n
        self.count = Counter()

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)

        if rootx == rooty:
            return False

        size_x = self.size[rootx]
        size_y = self.size[rooty]

        self.count[size_x] -= 1
        self.count[size_y] -= 1

        new_size = size_x + size_y

        self.parent[rooty] = rootx
        self.size[rootx] = new_size
        self.count[new_size] += 1

        return True

    def find(self, x):
        while x != self.parent[x]:
            # self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
