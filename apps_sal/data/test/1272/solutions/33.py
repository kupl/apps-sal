class UnionFind():
    # https://www.slideshare.net/chokudai/union-find-49066733
    # 作りたい要素数nで初期化
    # 使用するインスタンス変数の初期化
    def __init__(self, n):
        self.n = n
        # root[x]<0ならそのノードが根かつその値が木の要素数
        # rootノードでその木の要素数を記録する
        # root[x]>=0の場合は、特に直接的な意味を持たない気がする。計算に寄与するので意味はあるのだろうが。
        self.root = [-1] * (n + 1)
        # 木をくっつける時にアンバランスにならないように調整する
        # 無結合の時はRank=0,結合して1つ木が深くなると根がRank+=1
        self.rnk = [0] * (n + 1)

    # ノードxのrootノードを見つける
    #
    def Find_Root(self, x):
        if(self.root[x] < 0):
            return x
        else:
            # ここで代入しておくことで、後の繰り返しを避ける
            self.root[x] = self.Find_Root(self.root[x])
            return self.root[x]

    # 木の併合、入力は併合したい各ノード
    def Unite(self, x, y):
        # 入力ノードのrootノードを見つける
        x = self.Find_Root(x)
        y = self.Find_Root(y)
        # すでに同じ木に属していた場合
        if(x == y):
            return
        # 違う木に属していた場合rnkを見てくっつける方を決める
        # (1)xのランクの方が大きい(位置が深い)場合
        elif(self.rnk[x] > self.rnk[y]):
            self.root[x] += self.root[y]
            self.root[y] = x

        # (2)yのランクの方が大きい(位置が深い)場合 or 等しい場合
        # また等しい場合、引数の2つめのyの方のランクを1つ増やす
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            # rnkが同じ（深さに差がない場合）は1増やす
            if(self.rnk[x] == self.rnk[y]):
                self.rnk[y] += 1

    # xとyが同じグループに属するか判断
    # Return: True or False
    def isSameGroup(self, x, y):
        return self.Find_Root(x) == self.Find_Root(y)

    # ノードxが属する木のサイズを返す
    def Count(self, x):
        ret = -self.root[self.Find_Root(x)]
        # print(ret)
        return ret


############################################################################
N, M = map(int, input().split())
A = [0] * M
B = [0] * M
for i in range(M):
    A[i], B[i] = map(int, input().split())

conv = N * (N - 1) // 2
UN = UnionFind(N)
ans = [conv]
for j in range(M - 1, 0, -1):
    if UN.isSameGroup(A[j], B[j]):
        pass
    else:
        conv -= UN.Count(A[j]) * UN.Count(B[j])
    ans.append(conv)
    UN.Unite(A[j], B[j])

for p in ans[::-1]:
    print(p)
