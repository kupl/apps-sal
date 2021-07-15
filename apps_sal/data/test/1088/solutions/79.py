MOD = 998244353
from math import factorial
N, K = list(map(int, input().split()))
field = [list(map(int, input().split())) for i in range(N)]

class Union_Find:
    # 親管理リストと高さ管理リストを初期化し、
    # 要素N個のUnion-Find森を作成する。
    # 親管理リストは、基本的には自分のひとつ上の親を表すが、
    # 値が負の場合には、自身が最上位の親(リーダー)であることを表し、
    # 自分を含めたグループの人数を管理することとする
    def __init__(self, N):
        self.parent = [-1] * N
        self.rank = [0] * N
        self.group_count = N
        self.N = N
    
    # xの所属するグループのリーダーを返す
    def find(self, x):
        # 自分自身がリーダーなら、自分を返す
        if self.parent[x] < 0:
            return x

        # 再帰的に捜索し、見つかれば繋ぎ変えておく
        # (計算量が増える＝面倒くさいので)高さ管理は行わない
        par = self.find(self.parent[x])
        self.parent[x] = par
        return par

    # xとyのグループを統合する
    def unite(self, x, y):
        # それぞれのリーダーに対する操作を行うことになる
        x = self.find(x)
        y = self.find(y)

        # リーダーが同じなら何もする必要がない
        if x == y:
            return

        # 木の高さが同じ場合：
        # グループの人数を合計しつつ適当に繋ぎ、繋げられた方の高さを1増やす
        if self.rank[x] == self.rank[y]:
            self.parent[x] += self.parent[y]
            self.parent[y] = x
            self.rank[x] += 1
        
        # 木の高さが違うなら、低い方を高い方につなぐ
        elif self.rank[x] > self.rank[y]:
            self.parent[x] += self.parent[y]
            self.parent[y] = x
        else:
            self.parent[y] += self.parent[x]
            self.parent[x] = y
        
        # 統合された場合、グループ数は1減る
        self.group_count -= 1
    
    # xとyが同じグループかどうかを調べる
    def samep(self, x, y):
        return self.find(x) == self.find(y)

    # xの所属するグループのメンバーをリストで返す
    def get_group_member_list(self, x):
        x = self.find(x)
        return [i for i in range(self.N) if self.find(i) == x]
    
    # xの所属するグループのメンバー数を返す
    def get_group_member_count(self, x):
        x = self.find(x)
        return -self.parent[x]

    # 全ての{リーダー:グループメンバー数}を辞書形式で返す
    def get_all_groups(self):
        return {idx:-n for idx, n in enumerate(self.parent) if n < 0}

hg = Union_Find(N)
for i in range(N-1):
    h1 = field[i]
    for j in range(i,N):
        h2 = field[j]
        if all([True if x+y <= K else False for x, y in zip(h1, h2)]):
            hg.unite(i, j)

vg = Union_Find(N)
rotated = list(zip(*field))
for i in range(N-1):
    v1 = rotated[i]
    for j in range(i, N):
        v2 = rotated[j]
        if all([True if x+y <= K else False for x, y in zip(v1, v2)]):
            vg.unite(i, j)

result = 1
for value in list(hg.get_all_groups().values()):
    result *= factorial(value)
    result %= MOD

for value in list(vg.get_all_groups().values()):
    result *= factorial(value)
    result %= MOD

print(result)

