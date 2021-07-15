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
    if N % 2 == 1:
        print((0))
        return
    n = 10
    ans = 0
    while n <= N:
        ans += N // n
        n *= 5
    print(ans)


def __starting_point():
    N = int(input())
    solve(N)

    # # test
    # from random import randint
    # from func import random_str
    # solve()

__starting_point()
