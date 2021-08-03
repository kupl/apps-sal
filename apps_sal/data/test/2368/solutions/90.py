from operator import add


class Coloring_Union_Find():
    def __init__(self, N, f):
        """0,1,...,n-1を要素として初期化する.

        N:要素数
        f:2変数関数の合成
        """
        self.n = N
        self.parents = [-1] * N
        self.data = [0] * N
        self.rank = [0] * N
        self.f = f

    def find(self, x):
        """要素xの属している族を調べる.

        x:要素
        """
        V = []
        while self.parents[x] >= 0:
            V.append(x)
            x = self.parents[x]

        for v in V:
            self.parents[v] = x
        return x

    def union(self, x, y):
        """要素x,yを同一視する.

        x,y:要素
        """
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        self.data[x] = self.data[y] = self.f(self.data[x], self.data[y])

        if self.rank[x] > self.rank[y]:
            self.parents[x] += self.parents[y]
            self.parents[y] = x
        else:
            self.parents[y] += self.parents[x]
            self.parents[x] = y

            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def size(self, x):
        """要素xの属している要素の数.

        x:要素
        """
        return -self.parents[self.find(x)]

    def same(self, x, y):
        """要素x,yは同一視されているか?

        x,y:要素
        """
        return self.find(x) == self.find(y)

    def set(self, x, c):
        """要素xの属する成分の色をcに変更する.

        x:要素
        c:色
        """
        self.data[self.find(x)] = c
        return

    def look(self, x):
        """要素xの属する成分の色

        x:要素
        """
        return self.data[self.find(x)]

    def members(self, x):
        """要素xが属している族の要素.
        ※族の要素の個数が欲しいときはsizeを使うこと!!

        x:要素
        """
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        """族の名前のリスト
        """
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        """族の個数
        """
        return len(self.roots())

    def all_group_members(self):
        """全ての族の出力
        """
        X = {r: [] for r in self.roots()}
        for k in range(self.n):
            X[self.find(k)].append(k)
        return X

    def color_list(self):
        return [self.look(x) for x in range(self.n)]

    def color_map(self):
        return {x: self.look(x) for x in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

# ================================================


N, M = map(int, input().split())
A = [0] + list(map(int, input().split()))
B = [0] + list(map(int, input().split()))
X = [a - b for (a, b) in zip(A, B)]

U = Coloring_Union_Find(N + 1, add)
U.data = X.copy()

for _ in range(M):
    c, d = map(int, input().split())
    U.union(c, d)

if U.color_list() == [0] * (N + 1):
    print("Yes")
else:
    print("No")
