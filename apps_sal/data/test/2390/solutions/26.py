import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


class SegTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(N)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """

    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, left, right):
        """
        [left, right)のsegfuncしたものを得る
        left: index(0-index)
        right: index(0-index)
        """
        res = self.ide_ele
        left += self.num
        right += self.num
        while left < right:
            if left & 1:
                res = self.segfunc(res, self.tree[left])
                left += 1
            if right & 1:
                res = self.segfunc(res, self.tree[right - 1])
            left >>= 1
            right >>= 1
        return res


def resolve():
    (n, c) = list(map(int, input().split()))
    XY = [list(map(int, input().split())) for _ in range(n)]
    R1 = [0]
    prev = 0
    for (x, y) in XY:
        R1.append(R1[-1] + y - (x - prev))
        prev = x
    R2 = [0]
    prev = 0
    for (x, y) in XY[::-1]:
        R2.append(R2[-1] + y - (c - x - prev))
        prev = c - x
    res = max(max(R1), max(R2))
    seg1 = SegTree(R2, lambda x, y: max(x, y), 0)
    for i in range(1, n + 1):
        point1 = R1[i] - XY[i - 1][0]
        point2 = seg1.query(0, n + 1 - i)
        res = max(res, point1 + point2)
    seg2 = SegTree(R1, lambda x, y: max(x, y), 0)
    for i in range(1, n + 1):
        point1 = R2[i] - (c - XY[-i][0])
        point2 = seg2.query(0, n + 1 - i)
        res = max(res, point1 + point2)
    print(res)


def __starting_point():
    resolve()


__starting_point()
