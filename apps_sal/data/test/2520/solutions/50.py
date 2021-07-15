class UnionFind():
    """
        unionfindtree のクラス
            グループを管理するデータ構造.
            全てのメソッドの計算量が O(log(n)) よりも小さい
        init: 管理対象の個数 n を用いて初期化
        find: ある要素 x の親がどの要素か返す
        union: ある要素 x と y が属しているグループを結合して1つのグループとする
        msize: ある要素 x が属するグループの大きさを返す
    """
    def __init__(self, n):
        self.n = n
        self.parents = [-1]*n
        self.rank = [0]*n
        self.size = [1]*n

    def find(self, x):
        """
            ある要素 x の親の要素を見つけるメソッド
        """
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    
    def union(self, x, y):
        """
            ある要素 x, y の属するグループを結合するメソッド
            x と y のランク(子の数)の小さい方が結合先の親となる
        """
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.rank[x] < self.rank[y]:
            self.size[y] += self.size[x]
            self.parents[x] = y
        else:
            self.size[x] += self.size[y]
            self.parents[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def msize(self, x):
        """
            ある要素 x の属するグループの大きさを返すメソッド
        """
        return self.size[self.find(x)]

def main():
    N, M, K = list(map(int, input().split()))
    uf = UnionFind(N)
    friends = [0] * N
    for _ in range(M):
        A, B = list(map(int, input().split()))
        uf.union(A-1, B-1)
        friends[A-1] += 1
        friends[B-1] += 1
    for _ in range(K):
        C, D = list(map(int, input().split()))
        if uf.find(C-1) == uf.find(D-1):
            friends[C-1] += 1
            friends[D-1] += 1
    ans = []
    for i in range(N):
        ans.append(uf.msize(i) - friends[i] - 1)
    print((*ans))

def __starting_point():
    main()

__starting_point()
