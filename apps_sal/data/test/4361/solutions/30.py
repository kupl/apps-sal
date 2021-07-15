# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, K, h):
    h.sort()
    ans = 10 ** 9
    for i in range(K - 1, N):
        ans = min(ans, h[i] - h[i - (K - 1)])
    print(ans)


def __starting_point():
    N, K = list(map(int, input().split()))
    h = [int(input()) for _ in range(N)]
    solve(N, K, h)

    # # test
    # from random import randint
    # from func import random_str
    # N, K = 10 ** 5, 10 ** 5 // 5
    # h = [randint(1, 10 ** 9) for _ in range(N)]
    # solve(N, K, h)

__starting_point()
