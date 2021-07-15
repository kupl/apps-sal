# 解説と以下を参考に作成
# https://atcoder.jp/contests/abc105/submissions/17007379
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
import math


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N):
    if N == 0:
        print('0')
        return

    ans = ''
    while N != 0:
        # 1桁目が 1 or 0 かはNが奇数か偶数かによってのみ決まる.
        #  → 2 で割った余りから 1 or 0 を決定する.
        m = N % 2
        ans = str(m) + ans
        # 1桁目の情報を取り除いて(偶数にして)右シフトし, 次の桁についても同様に確認していく.
        # この時, 2(,4,6,...)桁目は負の要素となっているので, 1桁目(1 or 0)として判定するために正負を反転させる.
        N = (N - m) * (-1) >> 1
    print(ans)


def __starting_point():
    N = int(input())
    solve(N)

    # # test
    # from random import randint
    # from func import random_str
    # solve()

__starting_point()
