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

# edge=[cost, place, place] sorted by cost.
# place are expected to be 0 to N-1
# N : vertical count


def clascal(N, E, tree_count=1):
    #E[weight, vertical, vertical]
    tree = UnionFind(N)
    weight = 0
    counter = 0
    # E[w, A, B]
    for e in sorted(E):
        if counter >= N - 1:
            break
        if tree.ifSame(e[1], e[2]):
            continue
        else:
            tree.unite(e[1], e[2])
            weight += e[0]
            counter += 1
    return weight


# いつもここから
N = int(input())
X = []
Y = []
for i in range(N):
    x, y = list(map(int, input().split()))
    X.append((x, i))
    Y.append((y, i))
X.sort()
Y.sort()
diff = []
for i in range(N - 1):
    diff.append((X[i + 1][0] - X[i][0], X[i][1], X[i + 1][1]))
    diff.append((Y[i + 1][0] - Y[i][0], Y[i][1], Y[i + 1][1]))
diff.sort()
print((clascal(N, diff)))
