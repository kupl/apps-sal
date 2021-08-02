# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N):
    import math
    coins = [1] + \
            [6 ** i for i in range(1, int(math.log(N, 6)) + 2)] + \
            [9 ** i for i in range(1, int(math.log(N, 9)) + 2)]
    coins.sort()
    dp = [0] + [math.inf] * N
    for i in range(1, N + 1):
        for c in coins:
            if i - c < 0:
                break
            dp[i] = min(dp[i], dp[i - c] + 1)
    print((dp[N]))


def __starting_point():
    N = int(input())
    solve(N)

    # # test
    # from random import randint
    # from func import random_str
    # for i in range(1, 100 + 1):
    #     solve(i)


__starting_point()
