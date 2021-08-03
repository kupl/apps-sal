from bisect import bisect_left, bisect_right, insort_right


class SquareSkipList:
    def __init__(self, values=None, sorted_=False, square=1000, seed=42):
        # values: 初期値のリスト
        # sorted_: 初期値がソート済みであるか
        # square: 最大データ数の平方根
        # seed: 乱数のシード
        inf = float("inf")
        self.rand_y = seed
        self.square = square
        if values is None:
            self.layer1 = []
            self.layer0 = [[]]
        else:
            self.layer1 = layer1 = []
            self.layer0 = layer0 = []
            if not sorted_:
                values.sort()
            rand_depth = self.rand_depth
            l0 = []
            for v in values:
                if rand_depth():
                    layer0.append(l0)
                    l0 = []
                    layer1.append(v)
                else:
                    l0.append(v)
            layer0.append(l0)
        self.layer1.append(inf)

    def rand_depth(self):  # 32bit xorshift
        y = self.rand_y
        y ^= y << 13 & 0xffffffff
        y ^= y >> 17
        y ^= y << 5 & 0xffffffff
        self.rand_y = y
        return y % self.square == 0

    def add(self, x):  # 要素の追加
        layer1, layer0 = self.layer1, self.layer0
        if self.rand_depth():
            idx1 = bisect_right(layer1, x)
            layer1.insert(idx1, x)
            layer0_idx1 = layer0[idx1]
            idx0 = bisect_right(layer0_idx1, x)
            layer0.insert(idx1 + 1, layer0_idx1[idx0:])  # layer0 は dict で管理した方が良いかもしれない
            del layer0_idx1[idx0:]
        else:
            idx1 = bisect_right(layer1, x)
            insort_right(layer0[idx1], x)

    def remove(self, x):  # 要素の削除
        layer1, layer0 = self.layer1, self.layer0
        idx1 = bisect_left(layer1, x)
        if layer1[idx1] == x:
            del layer1[idx1]
            layer0[idx1] += layer0[idx1 + 1]
            del layer0[idx1 + 1]
        else:
            layer0_idx1 = layer0[idx1]
            del layer0_idx1[bisect_left(layer0_idx1, x)]

    def bisect_left(self, x):  # x 以上の最小の値を返す  O(log(n))
        layer1, layer0 = self.layer1, self.layer0
        idx1 = bisect_left(layer1, x)
        res = layer1[idx1]
        if res == x:
            return res
        layer0_idx1 = layer0[idx1]
        if layer0_idx1:
            idx0 = bisect_left(layer0_idx1, x)
            if idx0 == len(layer0_idx1):
                return res
            else:
                return layer0_idx1[idx0]
        else:
            return res

    def search_higher(self, x):  # x を超える最小の値を返す  O(log(n))
        layer1, layer0 = self.layer1, self.layer0
        idx1 = bisect_right(layer1, x)
        res = layer1[idx1]
        layer0_idx1 = layer0[idx1]
        if layer0_idx1:
            idx0 = bisect_right(layer0_idx1, x)
            if idx0 == len(layer0_idx1):
                return res
            else:
                return layer0_idx1[idx0]
        else:
            return res

    def search_lower(self, x):  # x 未満の最大の値を返す  O(log(n))
        layer1, layer0 = self.layer1, self.layer0
        idx1 = bisect_left(layer1, x)
        res = layer1[idx1]
        layer0_idx1 = layer0[idx1]
        if res != x:  # res > x
            if layer0_idx1:
                idx0 = bisect_left(layer0_idx1, x)
                if idx0 != 0:
                    return layer0_idx1[idx0 - 1]
            return layer1[idx1 - 1]  # layer0_idx1 が空の場合とすべて x 以上の場合
        else:
            idx0 = bisect_left(layer0_idx1, x)
            if idx0 == 0:  # layer0_idx1 が空の場合とすべて res で埋まっている場合
                return layer1[idx1 - 1]
            else:
                return layer0_idx1[idx0 - 1]

    def pop(self, idx):
        # 小さい方から idx 番目の要素を削除してその要素を返す（0-indexed）
        raise NotImplementedError  # 地味に実装が悩ましい

    def print(self):
        print(self.layer1)
        print(self.layer0)


def main():
    # 参考: https://atcoder.jp/contests/abc140/submissions/7477790
    n = int(input())
    p = list(map(int, input().split()))
    idx = [0] * n
    for i in range(0, n):
        idx[i] = i
    idx.sort(key=lambda i: - p[i])
    ssl = SquareSkipList()
    ssl.add(-1)
    ssl.add(n)
    ans = 0
    for i in idx:
        nex = ssl.search_higher(i)
        nexnex = ssl.search_higher(nex)
        pre = ssl.search_lower(i)
        prepre = ssl.search_lower(pre)
        if prepre != float("inf"):
            ans += p[i] * (pre - prepre) * (nex - i)
        if nexnex != float("inf"):
            ans += p[i] * (i - pre) * (nexnex - nex)
        ssl.add(i)
    print(ans)


main()
