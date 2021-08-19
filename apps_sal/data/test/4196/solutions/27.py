# 解説を参考に作成
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque

def gcd(a, b):
    """最大公約数"""
    a, b = (a, b) if a >= b else (b, a)
    if b == 0:
        return a
    return gcd(b, a % b)


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, A):
    L = [0] * N
    L[0] = A[0]
    for i in range(1, N):
        L[i] = gcd(A[i], L[i - 1])
    R = [0] * N
    R[-1] = A[-1]
    for i in range(1, N):
        R[-(i + 1)] = gcd(A[-(i + 1)], R[-i])
    ans = 0
    for i in range(N):
        if i == 0:
            ans = max(ans, R[i + 1])
        elif i == N - 1:
            ans = max(ans, L[i - 1])
        else:
            ans = max(ans, gcd(L[i - 1], R[i + 1]))
    print(ans)


def __starting_point():
    # S = input()
    N = int(input())
    # N, M = map(int, input().split())
    A = [int(i) for i in input().split()]
    # B = [int(i) for i in input().split()]
    # AB = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, A)

    # # test
    # from random import randint
    # from func import random_str
    # solve()


__starting_point()
