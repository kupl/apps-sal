# 解説を参考に作成
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(S, K):
    ans = ''
    for i in range(len(S)):
        if i + 1 == K:
            ans = S[i]
            break
        if S[i] != '1':
            ans = S[i]
            break
    print(ans)


def __starting_point():
    S = input()
    K = int(input())
    # N, M = map(int, input().split())
    # A = [int(i) for i in input().split()]
    # B = [int(i) for i in input().split()]
    # AB = [[int(i) for i in input().split()] for _ in range(N)]
    solve(S, K)

    # # test
    # from random import randint
    # from func import random_str
    # solve()

__starting_point()
