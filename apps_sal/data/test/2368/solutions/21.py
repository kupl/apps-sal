import sys


class Union_Find():
    def __init__(self, N):
        """0,1,...,n-1を要素として初期化する.

        N:要素数
        """
        self.n = N
        self.parents = [-1] * N
        self.rank = [0] * N

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

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


input = sys.stdin.readline
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

U = Union_Find(N)
for _ in range(M):
    c, d = map(int, input().split())
    U.union(c - 1, d - 1)

H = U.all_group_members()
F = True
for g in H:
    X = Y = 0
    for u in H[g]:
        X += A[u]
        Y += B[u]
    F = F & (X == Y)

if F:
    print("Yes")
else:
    print("No")
