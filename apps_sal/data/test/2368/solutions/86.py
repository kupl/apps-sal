from collections import defaultdict


class UnionFind(object):
    def __init__(self, n=1):
        self.par = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, x):
        """
        x が属するグループを探索して親を出す。
        """
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self, x, y):
        """
        x と y のグループを結合
        """
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                x, y = y, x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            self.par[y] = x
            self.size[x] += self.size[y]

    def is_same(self, x, y):
        """
        x と y が同じグループか否か
        """
        return self.find(x) == self.find(y)

    def get_size(self, x):
        """
        x が属するグループの要素数
        """
        x = self.find(x)
        return self.size[x]


N, M = map(int, input().split())
uf = UnionFind(N)
A = list(map(int, input().split()))
B = list(map(int, input().split()))
for i in range(M):
    c, d = map(int, input().split())
    c -= 1; d -= 1
    uf.union(c, d)

dic = defaultdict(int)
for i in range(N):
    par = uf.find(i)
    dif = A[i] - B[i]
    dic[par] += dif

# print(dic)
for v in dic.values():
    if v != 0:
        print("No"); return
print("Yes")
