# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, a):
    print((sum([ai - 1 for ai in a])))


def __starting_point():
    N = int(input())
    a = [int(i) for i in input().split()]
    solve(N, a)

    # # test
    # from random import randint
    # from func import random_str
    # solve()


__starting_point()
