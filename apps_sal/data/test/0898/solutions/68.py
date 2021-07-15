# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque

def divisor(x):
    """約数"""
    from math import floor
    re = []
    _x = floor(x ** 0.5)
    for i in range(1, _x + 1):
        if x % i == 0:
            re.append(i)
            if x // i != i:
                re.append(x // i)
    re.sort()
    return re


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, M):
    div = divisor(M)
    div.sort()
    ans = 0
    for d in div:
        if M // d >= N:
            ans = d
    print(ans)


def __starting_point():
    # S = input()
    # N = int(input())
    N, M = list(map(int, input().split()))
    # A = [int(i) for i in input().split()]
    # B = [int(i) for i in input().split()]
    # AB = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, M)

    # # test
    # from random import randint
    # from func import random_str
    # solve()

__starting_point()
