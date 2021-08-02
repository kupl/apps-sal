class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):  # 親を返す
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):  # 和集合の生成
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):  # 所属する集合の大きさ
        return -self.parents[self.find(x)]

    def same(self, x, y):  # 同じ集合に属しているか判定
        return self.find(x) == self.find(y)

    def members(self, x):  # 同じ集合に属する要素全列挙
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):  # 集合のリーダー全列挙
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):  # 集合の数
        return len(self.roots())

    def all_group_members(self):  # 辞書型,{(リーダーの番号):(その集合の要素全列挙)}
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


n, m = map(int, input().split())
l = []
for i in range(m):
    l.append(list(map(int, input().split())))
ans = 0
for i in range(m):
    a = UnionFind(n)
    for j in range(m):
        if i == j:
            continue
        a.union(l[j][0] - 1, l[j][1] - 1)
    if a.group_count() == 2:
        ans += 1
print(ans)
