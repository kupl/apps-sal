# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, M, PY):
    ken = [0] * (N + 1)
    PY = [PY[i] + [i] for i in range(M)]
    PY.sort(key=lambda x: x[1])
    for i in range(M):
        p, y, s = PY[i]
        ken[p] += 1
        PY[i].append(ken[p])
    PY.sort(key=lambda x: x[2])
    for p, y, s, n in PY:
        print((('000000' + str(p))[-6:] + ('000000' + str(n))[-6:]))


def __starting_point():
    N, M = list(map(int, input().split()))
    PY = [[int(i) for i in input().split()] for _ in range(M)]
    solve(N, M, PY)

    # # test
    # from random import randint, sample
    # from func import random_str
    # N, M = 10 ** 5, 10 ** 5
    # PY = sample([[randint(1, 5), 10 ** 8 - i] for i in range(M)], M)
    # solve(N, M, PY)

__starting_point()
