# https://atcoder.jp/contests/abc120/tasks/abc120_d
# Unionfind


n, m = list(map(int, input().split()))


class UnionFind:
    def __init__(self, n):
        self.n = n
        # 各要素の親要素の番号を格納するリスト
        # 根がルートの時は、グループの要素数を格納　最初は全て根で要素数1
        self.parents = [-1] * n

    # 再帰 groupの根を返す
    # 経路圧縮あり
    def find(self, x):
        # 0より小さい場合は根
        if self.parents[x] < 0:
            # indexを返す
            return x
        else:
            # 根になるまで親を辿る
            # 経路圧縮 根のindexが全ての親に再帰的につく
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    # groupを併合
    def union(self, x, y):
        # 根を探す
        x = self.find(x)
        y = self.find(y)

        # 最初から統合されている
        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x
        # 根のグループ数を追加 xの方グループの要素数が多い前提なので多い方に寄せる
        self.parents[x] += self.parents[y]
        # 親(根)のindexを入れる
        self.parents[y] = x

    # xのgroupのサイズ
    def size(self, x):
        return - self.parents[self.find(x)]

    # 根が同じか判定
    def same(self, x, y):
        return self.find(x) == self.find(y)

    # ルートが同じ要素を返す
    def members(self, x):
        root = self.find(x)
        # 根が同じ要素
        return [i for i, in range(self.n) if self.find(i) == root]

    # 全ての根の要素を返す
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    # グループの数を数える
    def group_count(self):
        return len(self.roots())

    # {root: [要素]}
    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}


edge = []
for _ in range(m):
    a, b = list(map(int, input().split()))
    edge.append((a - 1, b - 1))

ans = [n * (n - 1) // 2]

uf = UnionFind(n)
# 辺を後ろから追加していく
for a, b in reversed(edge):
    if not uf.same(a, b):
        ag = uf.size(a)
        bg = uf.size(b)
        uf.union(a, b)
        ans.append(ans[-1] - ag * bg)
    else:
        ans.append(ans[-1])

ans.pop()
for i in reversed(ans):
    print(i)

