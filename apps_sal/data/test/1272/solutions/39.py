n, m = map(int, input().split())
# 逆順にunionfind
from collections import defaultdict
class UnionFind:
    def __init__(self, n):
        class KeyDict(dict):
            # 辞書にないときの対応
            def __missing__(self,key):
                self[key] = key
                return key
        self.parent = KeyDict()
        self.rank = defaultdict(int)
        self.weight = defaultdict(lambda:1)

    # 根を探す
    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            # 経路圧縮
            # 自分自身じゃない場合は、上にさかのぼって検索(再帰的に)
            y = self.find(self.parent[x])
            self.parent[x] = y      #親の置き換え(圧縮)
            return self.parent[x]

    # 結合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        # 低い方を高い方につなげる(親のランクによる)
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
            self.weight[y] += self.weight[x]
            self.weight[x] = 0
        else:
            self.parent[y] = x
            self.weight[x] += self.weight[y]
            self.weight[y] = 0
        
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1


    # 判定
    def judge(self, x, y):
        return self.find(x) == self.find(y)

ps = []
for i in range(m):
    a,b = map(int, input().split())
    a -= 1
    b -= 1
    ps.append((a,b))

uf = UnionFind(n)
now = n*(n-1)//2
ans = [now]
for a, b in ps[::-1]:
    if not uf.judge(a,b):
        n1 = uf.weight[uf.find(a)]
        n2 = uf.weight[uf.find(b)]
        now += n1*(n1-1)//2 + n2*(n2-1)//2 - (n1+n2)*(n1+n2-1)//2
        uf.union(a,b)
    ans.append(now)

for a in ans[::-1][1:]:
    print(a)
