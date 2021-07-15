# 解説を参考に作成
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N):
    mod = 10 ** 9 + 7
    memo = [{} for _ in range(N + 1)]

    def check(last4):
        for i in range(4):
            x = list(last4)
            if i > 0:
                x[i], x[i - 1] = x[i - 1], x[i]
            if ''.join(x).count('AGC') >= 1:
                return False
        return True

    def dfs(memo, digit, last3):
        # last3文字 + digit文字 で条件を満たす個数を再帰取得する
        if last3 in memo[digit]:
            return memo[digit][last3]  # 計算済みの場合はそれを使用
        if digit == 0:
            return 1  # +0文字なのであればパターンは1のみ
        re = 0
        for c in 'AGCT':
            if check(last3 + c):
                re = (re + dfs(memo, digit - 1, last3[1:] + c)) % mod
        memo[digit][last3] = re
        return re

    print((dfs(memo, N, 'TTT')))  # 最初の3文字は入れ替えてAGCになりうる4文字に干渉しないものにする


def __starting_point():
    N = int(input())
    solve(N)

    # # test
    # from random import randint
    # from func import random_str
    # solve()

__starting_point()
