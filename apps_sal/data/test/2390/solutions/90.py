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
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
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


def segfunc(x, y):
    """
    区間(x,y)に対して行いたい操作の入力
    最小値：min(x,y)
    最大値：max(x,y)
    和：x + y
    積：x * y
    最大公約数：math.gcd(x, y)
    """
    return max(x, y)


ide_ele = -f_inf


def resolve():
    n, c = list(map(int, input().split()))
    XV = [list(map(int, input().split())) for _ in range(n)]

    R = [0]
    prev = 0
    for i in range(n):
        x, v = XV[i]
        R.append(R[-1] + v - (x - prev))
        prev = x
    seg = SegTree(R, segfunc, ide_ele)

    R_r = [0]
    prev_r = 0
    for i in reversed(list(range(n))):
        x_r, v_r = XV[i]
        x_r = c - x_r
        R_r.append(R_r[-1] + v_r - (x_r - prev_r))
        prev_r = x_r
    seg_r = SegTree(R_r, segfunc, ide_ele)

    res1 = max(R)
    res2 = max(R_r)
    res3 = 0
    for i in range(1, n + 1):
        right = R[i] - XV[i - 1][0]
        idx = n + 1 - i
        left = seg_r.query(0, idx)
        res3 = max(res3, right + left)
    res4 = 0
    for i in range(1, n + 1):
        left_r = R_r[i] - (c - XV[-i][0])
        idx_r = n + 1 - i
        right_r = seg.query(0, idx_r)
        res4 = max(res4, left_r + right_r)
    print((max(res1, res2, res3, res4)))


def __starting_point():
    resolve()


__starting_point()
