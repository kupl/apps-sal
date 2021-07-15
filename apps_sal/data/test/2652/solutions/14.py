class UnionFind():
    # 初めは全ての頂点が別々の木の根
    def __init__(self, n):  # n要素で初期化
        self.parent = list(range(n)) # 親
        self.rank = [0] * n   # 木の深さ

    def root_of(self, x):
        children = [x]
        while self.parent[x] != x:
            x = self.parent[x]
            children.append(x)

        for ch in children:
            self.parent[ch] = x
        return x

    # xとyの属する集合を併合
    def union(self, x, y):
        rx = self.root_of(x)
        ry = self.root_of(y)
        if rx == ry:
            return
        if self.rank[rx] < self.rank[ry]: # ランクの小さい木から大きい木の根に辺を張る
            self.parent[rx] = ry  # rxをryの子とする
        else:
            self.parent[ry] = rx
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1

    # 同じ集合に属するかどうか
    def same(self, x, y):
        return self.root_of(x) == self.root_of(y)


N = int(input())
X = [None] * N
Y = [None] * N
for i in range(N):
    x, y = [int(x) for x in input().split()]
    X[i] = (x, i)
    Y[i] = (y, i)

X.sort()
Y.sort()
E = []
xp = X[0][0]
ip = X[0][1]
for (x, i) in X:
    E.append((x - xp, (ip, i)))
    xp = x
    ip = i

yp = Y[0][0]
ip = Y[0][1]
for (y, i) in Y:
    E.append((y - yp, (ip, i)))
    yp = y
    ip = i

E.sort()
uf = UnionFind(N)
cost = 0
for c, (e1, e2) in E:
    if uf.same(e1, e2): continue
    cost += c
    uf.union(e1, e2)

print(cost)
