# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, hi):
    ans = 0
    for i in range(max(hi)):
        flg = False
        for n in range(N):
            if hi[n] != 0:
                if not flg:
                    flg = True
                    ans += 1
                hi[n] -= 1
            else:
                flg = False
    print(ans)


def __starting_point():
    # S = input()
    N = int(input())
    # N, M = map(int, input().split())
    hi = [int(i) for i in input().split()]
    # Bi = [int(i) for i in input().split()]
    # ABi = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, hi)

    # # test
    # from random import randint
    # from func import random_str
    # solve()


__starting_point()
