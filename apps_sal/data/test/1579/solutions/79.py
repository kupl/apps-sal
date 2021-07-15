class UnionFind :
    def __init__(self, size) :
        self.parent = list(range(size))
        self.height = [0] * size
        self.size = [1] * size
        self.component = size

    def root(self, index) :
        if self.parent[index] == index :  # 根の場合
            return index
        rootIndex = self.root(self.parent[index])  # 葉の場合親の根を取得
        self.parent[index] = rootIndex  # 親の付け直し
        return rootIndex

    def union(self, index1, index2) :  # 結合
        root1 = self.root(index1)
        root2 = self.root(index2)

        if root1 == root2 :  # 連結されている場合
            return

        self.component -= 1  # 連結成分を減らす

        if self.height[root1] < self.height[root2] :
            self.parent[root1] = root2  # root2に結合
            self.size[root2] += self.size[root1]
        else :
            self.parent[root2] = root1  # root1に結合
            self.size[root1] += self.size[root2]
            if self.height[root1] == self.height[root2] :
                self.height[root1] += 1
        return

    def isSameRoot(self, index1, index2) :
        return self.root(index1) == self.root(index2)

    def sizeOfSameRoot(self, index) :
        return self.size[self.root(index)]

    def getComponent(self) :
        return self.component

N = int(input())
R = 10**5 + 10
IXY = []

for i in range(N):
    x, y = list(map(int, input().split()))
    IXY.append((i, x, y))

X = [[] for _ in range(R)]
Y = [[] for _ in range(R)]
for i, x, y in IXY:
    X[x].append(i)
    Y[y].append(i)

tree = UnionFind(N)

for x in X:
    for fr, to in zip(x, x[1:]):
        tree.union(fr, to)
for y in Y:
    for fr, to in zip(y, y[1:]):
        tree.union(fr, to)

G = [[0, set(), set()] for _ in range(N)]
for i, x, y in IXY:
    r = tree.root(i)
    G[r][0] += 1
    G[r][1].add(x)
    G[r][2].add(y)

ans = 0
for grp in G:
    if grp[0] < 3:
        continue
    x = len(grp[1])
    y = len(grp[2])
    A = x * y
    ans += max(0, A - grp[0])
print(ans)

