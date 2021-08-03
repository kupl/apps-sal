class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return set([i for i in range(self.n) if self.find(i) == root])

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())


n, m, k = list(map(int, input().split()))
# 集合で見ていくのが一番速いのでunionfindを扱う
friend_un = UnionFind(n)
# 答え用のlist
lst = [0] * n
for _ in range(m):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    # 友達同士で同じ集合を形成していくことで、数の集計が楽になる
    friend_un.union(a, b)
    # 友達候補には友達同士は含まないので、答え用のリストには予め1減らしておく
    lst[a] -= 1
    lst[b] -= 1
for _ in range(k):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    # ブロック同士が同じ集合内にいた場合、これも友達候補には含めないので答え用のリストには1減らしておく
    if friend_un.same(a, b):
        lst[a] -= 1
        lst[b] -= 1
for i in range(n):
    # 自分の数も含めているので1減らしておく
    lst[i] += friend_un.size(i) - 1
print((' '.join([str(i) for i in lst])))
