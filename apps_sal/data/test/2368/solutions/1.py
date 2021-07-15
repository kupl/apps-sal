class UnionFind:
    def __init__(self, n):
        # n: 頂点数
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        # xの根
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        # 無向辺をはる
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def members(self, x):
        # xの属する集団の頂点の列挙
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        # すべての根の要素を列挙
        return [i for i, x in enumerate(self.parents) if x < 0]

    def all_group_members(self):
        # 根ごとの集団要素列挙
        return {r: self.members(r) for r in self.roots()}

N,M=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
UF = UnionFind(N)
for _ in range(M):
  c,d=map(int,input().split())
  UF.union(c-1,d-1)
a_sum = [0] * N
b_sum = [0] * N
for i,(a,b) in enumerate(zip(A,B)):
  a_sum[UF.find(i)] += a
  b_sum[UF.find(i)] += b
for ai,bi in zip(a_sum,b_sum):
  if ai != bi:
    print('No')
    break
else:
  print('Yes')
