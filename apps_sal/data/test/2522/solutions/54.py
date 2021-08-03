# 解説を参考に作成
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, Ai, Bi):
    Ci = [0] * (N + 1)
    Di = [0] * (N + 1)
    j = 0
    k = 0
    for i in range(1, N + 1):
        while j < N and Ai[j] <= i:
            j += 1
        Ci[i] = j
        while k < N and Bi[k] <= i:
            k += 1
        Di[i] = k
    # print(Ci)
    # print(Di)
    for i in range(1, N + 1):
        if Ci[i] - Ci[i - 1] + Di[i] - Di[i - 1] > N:
            print('No')
            return
    x = 0
    for i in range(1, N + 1):
        x = max(x, Ci[i] - Di[i - 1])
    print('Yes')
    # print(x)
    # print(' '.join([str(a) for a in Ai]))
    print((' '.join([str(Bi[(N - x + i) % N]) for i in range(N)])))


def __starting_point():
    # S = input()
    N = int(input())
    # N, M = map(int, input().split())
    Ai = [int(i) for i in input().split()]
    Bi = [int(i) for i in input().split()]
    # ABi = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, Ai, Bi)

    # # test
    # from random import randint
    # from func import random_str
    # solve()


__starting_point()
