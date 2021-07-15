from collections import defaultdict
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):  #要素xが属するグループの根を返す
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):  #要素xが属するグループと要素yが属するグループを併合
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):  #グループのサイズ
        return -self.parents[self.find(x)]

    def same(self, x, y):   #要素xと要素yが同じグループかどうか
        return self.find(x) == self.find(y)

    def members(self, x):   #要素xが属するグループに属する要素をリストで返す
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):    #すべての根の要素をリストで返す
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):  #グループの数を変えす
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

n, k, l = map(int, input().split())

uf = UnionFind(n)

p, q = [0] * k, [0] * k
for i in range(k):
    pp, qq = map(int, input().split())
    p[i] = pp - 1 
    q[i] = qq - 1
    uf.union(pp - 1, qq - 1)

uuff = UnionFind(n)
r, s = [0] * l, [0] * l
for i in range(l):
    rr, ss = map(int, input().split())
    r[i] = rr - 1
    s[i] = ss - 1
    uuff.union(rr - 1, ss - 1)
dic = defaultdict(int)
for i in range(n):
    dic[(uf.find(i), uuff.find(i))] += 1

ans = []
for i in range(n):
    ans.append(dic[uf.find(i), uuff.find(i)])

for i in ans:
    print(i,end=" ")
