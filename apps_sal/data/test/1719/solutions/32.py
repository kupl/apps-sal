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
    dp = [{} for _ in range(N + 1)]
    dp[0].setdefault('TTT', 1)

    def check(last4):
        for i in range(4):
            x = list(last4)
            if i > 0:
                x[i], x[i - 1] = x[i - 1], x[i]
            if ''.join(x).count('AGC') >= 1:
                return False
        return True

    for i in range(1, N + 1):
        for last3, count in list(dp[i - 1].items()):
            for c in 'AGCT':
                if check(last3 + c):
                    new_last3 = last3[1:] + c
                    dp[i].setdefault(last3[1:] + c, 0)
                    dp[i][new_last3] = (dp[i][new_last3] + count) % mod

    print((sum(dp[-1].values()) % mod))


def __starting_point():
    N = int(input())
    solve(N)

    # # test
    # from random import randint
    # from func import random_str
    # solve()

__starting_point()
