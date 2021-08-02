# 解説を参考に作成
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, A, B):
    buf = -1
    key = 0
    for i in range(N):
        if buf != A[i]:
            key = 0  # 前回(A[i - 1])と同じ値じゃなければリセット
        if A[i] == B[i]:
            for j in range(key, N):
                if A[i] != A[j] and B[j] != A[i]:
                    B[i], B[j] = B[j], B[i]
                    key = j
                    break
            else:
                print('No')
                return
        buf = A[i]
    print('Yes')
    print((' '.join([str(i) for i in B])))


def __starting_point():
    # S = input()
    N = int(input())
    # N, M = map(int, input().split())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    # ABi = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, A, B)

    # # test
    # from random import randint
    # from func import random_str
    # solve()


__starting_point()
