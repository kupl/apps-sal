from collections import Counter

class UnionFind():
    # 作りたい要素数nで初期化
    # 使用するインスタンス変数の初期化
    def __init__(self, n):
        self.n = n
        # root[x]<0ならそのノードが根かつその値が木の要素数
        # rootノードでその木の要素数を記録する
        self.root = [-1]*(n+1)
        # 木をくっつける時にアンバランスにならないように調整する
        self.rnk = [0]*(n+1)

    # ノードxのrootノードを見つける
    def find_root(self, x):
        if(self.root[x] < 0):
            return x
        else:
            # ここで代入しておくことで、後の繰り返しを避ける
            #経路圧縮
            self.root[x] = self.find_root(self.root[x])
            return self.root[x]
    # 木の併合、入力は併合したい各ノード
    def unite(self, x, y):
        # 入力ノードのrootノードを見つける
        x = self.find_root(x)
        y = self.find_root(y)
        # すでに同じ木に属していた場合
        if(x == y):
            return
        # 違う木に属していた場合rnkを見てくっつける方を決める
        elif(self.rnk[x] > self.rnk[y]):
            self.root[x] += self.root[y]
            self.root[y] = x

        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            # rnkが同じ（深さに差がない場合）は1増やす
            if(self.rnk[x] == self.rnk[y]):
                self.rnk[y] += 1
    # xとyが同じグループに属するか判断
    def isSame(self, x, y):
        return self.find_root(x) == self.find_root(y)

    # ノードxが属する木のサイズを返す
    def size(self, x):
        return -self.root[self.find_root(x)]
        
n,k,l = map(int,input().split())
fe = UnionFind(n)
bus = UnionFind(n)
for _ in range(k):
    p,q = map(int,input().split())
    fe.unite(p,q)
for _ in range(l):
    r,s = map(int,input().split())
    bus.unite(r,s)
cnt = Counter()
for i in range(1,n+1):
    cnt[fe.find_root(i),bus.find_root(i)] += 1

print(*[cnt[fe.find_root(i),bus.find_root(i)]for i in range(1,n+1)])
