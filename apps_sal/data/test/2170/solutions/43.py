# 解説などを参考に作成
# https://mathtrain.jp/hojo
# https://qiita.com/DaikiSuyama/items/4d0388a3f68b60c3e5f3
# https://atcoder.jp/contests/abc172/submissions/16541798
# tag: 包除原理
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque

class FermatCmb:
    """フェルマー小定理を使用した順列, 組み合わせ計算"""

    def __init__(self, max_num, mod):
        """
        :param max_num: max n of nCk
        :param mod: any prime number
        """
        self.max_num = max_num
        self.mod = mod
        self.fact = [0 for _ in range(max_num + 1)]
        self.factinv = [0 for _ in range(max_num + 1)]

        self.fact[0] = 1
        for i in range(1, max_num + 1):
            self.fact[i] = (i * self.fact[i - 1]) % self.mod

        self.factinv[-1] = pow(self.fact[-1], mod - 2, mod)
        for i in range(max_num, 0, -1):
            self.factinv[i - 1] = self.factinv[i] * i
            self.factinv[i - 1] %= self.mod

    def nCk(self, n, k):
        return (self.fact[n] * self.factinv[k] * self.factinv[n - k]) % self.mod

    def nPk(self, n, k):
        return (self.fact[n] * self.factinv[n - k]) % self.mod


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, M):
    mod = 10 ** 9 + 7
    cf = FermatCmb(M, mod)
    ans = 0
    for k in range(N + 1):
        ans += (-1) ** k * cf.nCk(N, k) * cf.nPk(M, k) * (
            cf.nPk(M - k, N - k) ** 2)
        ans %= mod
    print(ans)


def __starting_point():
    # S = input()
    # N = int(input())
    N, M = list(map(int, input().split()))
    # A = [int(i) for i in input().split()]
    # B = [int(i) for i in input().split()]
    # AB = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, M)

    # # test
    # from random import randint
    # from func import random_str
    # solve()


__starting_point()
