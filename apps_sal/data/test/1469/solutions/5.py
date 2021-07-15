# 解説を参考に作成
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
# 
# 
# @stop_watch
def solve(L):
    import math
    N = int(math.log2(L))
    grahp = []
    for i in range(1, N + 1):
        grahp.append([i, i + 1, 0])
        grahp.append([i, i + 1, 2 ** (i - 1)])
    for i in range(N, 0, -1):
        if L - 2 ** (i - 1) >= 2 ** N:
            L = L - 2 ** (i - 1)
            grahp.append([i, N + 1, L])
    M = len(grahp)

    print(N + 1, M)
    [print(' '.join([str(i) for i in g])) for g in grahp]



def __starting_point():
    # S = input()
    L = int(input())
    # N, M = map(int, input().split())
    # A = [int(i) for i in input().split()]
    # B = [int(i) for i in input().split()]
    # AB = [[int(i) for i in input().split()] for _ in range(N)]
    solve(L)

    # # test
    # from random import randint
    # from func import random_str
    # solve()

__starting_point()
