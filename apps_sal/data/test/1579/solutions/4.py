from collections import defaultdict


class UnionFind:

    def __init__(self, size):
        self.parent = list(range(size))
        self.height = [0] * size
        self.size = [1] * size
        self.componentCount = size

    def root(self, index):
        if self.parent[index] == index:
            return index
        rootIndex = self.root(self.parent[index])
        self.parent[index] = rootIndex
        return rootIndex

    def union(self, index1, index2):
        root1 = self.root(index1)
        root2 = self.root(index2)
        if root1 == root2:
            return
        self.componentCount -= 1
        if self.height[root1] < self.height[root2]:
            self.parent[root1] = root2
            self.size[root2] += self.size[root1]
        else:
            self.parent[root2] = root1
            self.size[root1] += self.size[root2]
            if self.height[root1] == self.height[root2]:
                self.height[root1] += 1
        return

    def isSameRoot(self, index1, index2):
        return self.root(index1) == self.root(index2)

    def sizeOfSameRoot(self, index):
        return self.size[self.root(index)]


N = int(input())
XY = [tuple(map(int, input().split())) for _ in range(N)]
xGrp = defaultdict(list)
yGrp = defaultdict(list)
for (i, (x, y)) in enumerate(XY):
    xGrp[x].append(i)
    yGrp[y].append(i)
tree = UnionFind(N)
for grp in list(xGrp.values()):
    for (l, r) in zip(grp, grp[1:]):
        tree.union(l, r)
for grp in list(yGrp.values()):
    for (l, r) in zip(grp, grp[1:]):
        tree.union(l, r)
xGrpList = defaultdict(set)
yGrpList = defaultdict(set)
for (i, (x, y)) in enumerate(XY):
    xGrpList[tree.root(i)].add(x)
    yGrpList[tree.root(i)].add(y)
ans = 0
for i in range(N):
    if i != tree.root(i):
        continue
    (X, Y) = (xGrpList[i], yGrpList[i])
    if len(X) + len(Y) < 3:
        continue
    A = len(X) * len(Y)
    ans += A - tree.sizeOfSameRoot(i)
print(ans)
