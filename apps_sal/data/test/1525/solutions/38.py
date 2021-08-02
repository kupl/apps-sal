# 解説と下記を参考に作成
# https://atcoder.jp/contests/abc113/submissions/15821617
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(H, W, K):
    mod = 10 ** 9 + 7
    dp = [[0] * W for _ in range(H + 1)]
    dp[0][0] = 1
    fibo = [1, 2, 3, 5, 8, 13, 21]
    for h in range(H):
        for w in range(W):
            if dp[h][w] == 0:
                continue
            for i in range(3):
                new_w = w - 1 + i
                if not 0 <= new_w < W:
                    continue
                l, r = min(w, new_w), max(w, new_w)
                tmp = fibo[max(l - 1, 0)] * fibo[max(W - 1 - (r + 1), 0)]
                dp[h + 1][new_w] += dp[h][w] * tmp
                dp[h + 1][new_w] %= mod
    print((dp[-1][K - 1]))


def __starting_point():
    H, W, K = list(map(int, input().split()))
    solve(H, W, K)

    # # test
    # from random import randint
    # from func import random_str
    # solve()


__starting_point()
