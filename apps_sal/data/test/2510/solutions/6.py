# n, m = map(int, input().split())
# graph = [[] for i in range(n+1)]

# for i in range(m):
#     a, b = map(int, input().split())
#     graph[a] += [b]
#     graph[b] += [a]
# print(graph)
# nex = [i for i in range(1, n+1)]
# tmp = []
# ans = 0
# for i in range(1, n+1):
#     if i in nex:
#         for j in graph[i]:
#             if j in nex:
#                 tmp.append(j)
#         ans += 1
#         print(tmp)
#         nex = tmp
# print(ans)


#O(α(n)) < O(log(n))
class UnionFind():

    def __init__(self, n):
        self.par = []
        self.rank = []
        for i in range(n):
            self.par.append(i)  # 自身を親としてinit
            self.rank.append(1)  # １つのノードをrank1としてカウント

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])  # 親の更新も同時に行う
            return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x != y:
            if self.rank[x] <= self.rank[y]:
                x, y = y, x

            # rankが小さい方を大きい方につなげる
            self.par[y] = x

            # 親のrankに繋いだ木のrankを全て足す
            self.rank[x] += self.rank[y]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return self.rank[self.find(x)]


n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]

ans = 0
uf = UnionFind(n)

for a, b in ab:
    uf.unite(a - 1, b - 1)

for i in range(n):
    ans = max(ans, uf.size(i))

print(ans)
