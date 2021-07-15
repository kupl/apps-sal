# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
# 
# 
# @stop_watch
def solve(N, Q, S, LRi):
    cumulative_sum = [0, 0]
    for i in range(1, N):
        tmp = cumulative_sum[-1]
        if S[i - 1:i + 1] == 'AC':
            tmp += 1
        cumulative_sum.append(tmp)

    for l, r in LRi:
        print((cumulative_sum[r] - cumulative_sum[l]))


def __starting_point():
    N, Q = list(map(int, input().split()))
    S = input()
    LRi = [[int(i) for i in input().split()] for _ in range(Q)]
    solve(N, Q, S, LRi)

    # # test
    # from random import randint
    # from func import random_str
    # N, Q = 10 ** 5, 10 ** 5
    # S = random_str(N, 'ACGT')
    # LRi = [sorted([randint(1, N) for _ in range(2)]) for _ in range(Q)]
    # solve(N, Q, S, LRi)

__starting_point()
