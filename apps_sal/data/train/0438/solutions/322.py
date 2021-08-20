class UnionFind:

    def __init__(self):
        self.parent = dict()
        self.rank = dict()
        self.size = dict()
        self.sizes = collections.defaultdict(int)
        return

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
            self.size[x] = 1
            self.sizes[1] += 1
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        while self.parent[x] != root:
            parent = self.parent[x]
            self.parent[x] = root
            x = parent
        return root

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        if self.size[x_root] < self.size[y_root]:
            (x_root, y_root) = (y_root, x_root)
        y_size = self.size[y_root]
        x_size = self.size[x_root]
        self.sizes[x_size] -= 1
        self.sizes[y_size] -= 1
        self.parent[y_root] = x_root
        self.size[x_root] += self.size[y_root]
        self.sizes[self.size[x_root]] += 1
        return


class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        binary_string = [0] * n
        uf = UnionFind()
        max_step = -1
        step = 1
        for i in arr:
            index = i - 1
            binary_string[index] = 1
            root = uf.find(i)
            if index - 1 >= 0 and binary_string[index - 1] == 1:
                uf.union(root, i - 1)
            if index + 1 < len(binary_string) and binary_string[index + 1] == 1:
                uf.union(root, i + 1)
            if uf.sizes[m] > 0:
                max_step = step
            step += 1
        return max_step
