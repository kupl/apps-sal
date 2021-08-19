class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.depth = [0 for i in range(n)]
        self.size = [0 for i in range(n)]
        self.count = collections.defaultdict(int)

    def findParent(self, n):
        if self.parent[n] != n:
            self.parent[n] = self.findParent(self.parent[n])
        return self.parent[n]

    def union(self, x, y):
        x_parent = self.findParent(x)
        y_parent = self.findParent(y)

        if x_parent == y_parent:
            return

        self.count[self.size[y_parent]] -= 1
        self.count[self.size[x_parent]] -= 1

        if self.depth[x_parent] >= self.depth[y_parent]:
            self.parent[y_parent] = x_parent
            self.size[x_parent] += self.size[y_parent]
            self.depth[x_parent] += (self.depth[x_parent] == self.depth[y_parent])

            self.count[self.size[x_parent]] += 1

        else:
            self.parent[x_parent] = y_parent
            self.size[y_parent] += self.size[x_parent]
            self.depth[y_parent] += 1

            self.count[self.size[y_parent]] += 1


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        last_step = -1
        bits = [0] * len(arr)
        dsu = DSU(len(arr))

        for i in range(len(arr)):
            idx = arr[i] - 1
            bits[idx] = 1

            dsu.size[idx] = 1
            dsu.count[1] += 1

            cur_size = 1

            if idx > 0:
                if bits[idx - 1]:
                    dsu.union(idx - 1, idx)
            if idx < len(arr) - 1:
                if bits[idx + 1]:
                    dsu.union(idx + 1, idx)
            if dsu.count[m] > 0:
                last_step = i + 1

            # print(dsu.parent)
            # print(dsu.size)
            # print(dsu.count)
            # print()

        return last_step
