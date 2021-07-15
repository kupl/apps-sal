# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, X):
    layer = [1]
    pate = [1]
    for _ in range(N):
        layer.append(layer[-1] * 2 + 3)
        pate.append(pate[-1] * 2 + 1)

    # print(layer[-1])
    # print(pate[-1])

    def burger(n, l):
        if layer[n] <= l:
            return pate[n]
        if l == 0:
            return 0
        re = 0
        if layer[n] // 2 + 1 <= l:
            re += pate[n - 1] + 1  # center pattie
            l -= layer[n] // 2 + 1
        else:
            l -= 1  # first bun
        re += burger(n - 1, l)
        return re

    print((burger(N, X)))


def __starting_point():
    N, X = list(map(int, input().split()))
    solve(N, X)

    # # test
    # from random import randint
    # from func import random_str
    # N, X = 3, 1
    # for i in range(1, 29 + 1):
    #     solve(N, i)

__starting_point()
