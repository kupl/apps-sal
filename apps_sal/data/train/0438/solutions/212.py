class UnionFind:

    def __init__(self, values: int):
        self.values = list(range(values))
        self.connectedComponents = [1] * values

    def root(self, key):
        root = self.values[key]

        while root != self.values[root]:
            root = self.values[root]

        return root

    def union(self, keyA, keyB):
        rootA = self.root(keyA)
        rootB = self.root(keyB)

        self.values[rootB] = rootA
        self.connectedComponents[rootA] += self.connectedComponents[rootB]
        self.connectedComponents[rootB] = 0

    def find(self, keyA, keyB):
        return self.root(keyA) == self.root(keyB)


class Solution:
    def findLatestStep(self, arr: list, m: int) -> int:

        uf = UnionFind(len(arr))

        step = -1
        groupM = set()
        binaryString = [0] * len(arr)

        for i, val in enumerate(arr):

            if i == 9:
                print('')

            val = val - 1

            binaryString[val] = 1

            if val != 0 and binaryString[val - 1] == 1:
                if not uf.find(val, val - 1):
                    root = uf.root(val - 1)
                    uf.union(val, val - 1)

                    if root in groupM:
                        groupM.remove(root)

            if val != (len(arr) - 1) and binaryString[val + 1] == 1:
                if not uf.find(val, val + 1):
                    root = uf.root(val + 1)
                    uf.union(val, val + 1)

                    if root in groupM:
                        groupM.remove(root)

            if uf.connectedComponents[val] == m:
                groupM.add(val)
            elif uf.connectedComponents[val] != m and val in groupM:
                groupM.remove(val)

            if len(groupM):
                step = i + 1

        return step
