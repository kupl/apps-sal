class UnionFind:
    # この時点でそれぞれのノードは自分を親としている
    # 初期化時に問題が0の頂点を認めるかに注意すること
    def __init__(self, n):
        self.N = n
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    # xの根を返す関数
    def root(self, x):
        visited_nodes = []
        while True:
            p = self.parent[x]
            if p == x:
                # 縮約
                for node in visited_nodes:
                    self.parent[node] = x
                return x
            else:
                visited_nodes.append(x)
                x = p

    # 木の結合を行う。親の配下に入る
    def unite(self, x, y):
        if not self.root(x) == self.root(y):
            if self.rank[x] > self.rank[y]:
                self.parent[self.root(y)] = self.root(x)
            else:
                self.parent[self.root(x)] = self.root(y)
                if self.rank[x] == self.rank[y]:
                    self.rank[self.root(y)] += 1

    def ifSame(self, x, y):
        return self.root(x) == self.root(y)

    # 木の根に到達すまでにたどるノードの配列を返す
    def printDebugInfo(self):
        print([self.root(i) for i in range(self.N)])

    def seikei(self):
        for i in range(self.N):
            self.root(i)


N, M = list(map(int, input().split()))
tree = UnionFind(N)
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
for _ in range(M):
    c, d = list(map(int, input().split()))
    tree.unite(c - 1, d - 1)

tree.seikei()

gruops = {}
for i, x in enumerate(tree.parent):
    if x in gruops:
        gruops[x].append(i)
    else:
        gruops[x] = [i]


for k in list(gruops.keys()):
    a_total = 0
    b_total = 0
    for x in gruops[k]:
        a_total += A[x]
        b_total += B[x]
    if not a_total == b_total:
        print('No')
        return
print('Yes')
