# -*- coding: utf-8 -*-

import sys


def input(): return sys.stdin.readline().strip()
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
def list4d(a, b, c, d, e): return [[[[e] * d for j in range(c)] for j in range(b)] for i in range(a)]
def ceil(x, y=1): return int(-(-x // y))
def INT(): return int(input())
def MAP(): return list(map(int, input().split()))
def LIST(N=None): return list(MAP()) if N is None else [INT() for i in range(N)]
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')


sys.setrecursionlimit(10 ** 9)
INF = 10 ** 18
MOD = 10 ** 9 + 7


class ModTools:
    """ 階乗たくさん使う時用のテーブル準備 """

    def __init__(self, MAX, MOD):
        """ MAX：階乗に使う数値の最大以上まで作る """

        MAX += 1
        self.MAX = MAX
        self.MOD = MOD
        # 階乗テーブル
        factorial = [1] * MAX
        factorial[0] = factorial[1] = 1
        for i in range(2, MAX):
            factorial[i] = factorial[i - 1] * i % MOD
        # 階乗の逆元テーブル
        inverse = [1] * MAX
        # powに第三引数入れると冪乗のmod付計算を高速にやってくれる
        inverse[MAX - 1] = pow(factorial[MAX - 1], MOD - 2, MOD)
        for i in range(MAX - 2, 0, -1):
            # 最後から戻っていくこのループならMAX回powするより処理が速い
            inverse[i] = inverse[i + 1] * (i + 1) % MOD
        self.fact = factorial
        self.inv = inverse

    def nCr(self, n, r):
        """ 組み合わせの数 (必要な階乗と逆元のテーブルを事前に作っておく) """

        if n < r:
            return 0
        # 10C7 = 10C3
        r = min(r, n - r)
        # 分子の計算
        numerator = self.fact[n]
        # 分母の計算
        denominator = self.inv[r] * self.inv[n - r] % self.MOD
        return numerator * denominator % self.MOD

    def div(self, x, y):
        """ MOD除算 """

        return x * pow(y, self.MOD - 2, self.MOD) % self.MOD


r1, c1, r2, c2 = MAP()

mt = ModTools(r2 + c2 + 2, MOD)


def calc(r, c):
    return mt.div(((r + 2) * mt.nCr(c + r + 2, r + 2) - c - 1), (c + 1))


ans = calc(r2, c2) - calc(r2, c1 - 1) - calc(r1 - 1, c2) + calc(r1 - 1, c1 - 1)
print((ans % MOD))
