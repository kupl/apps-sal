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
def solve(N, X, x):
    x_abs = [abs(X - xi) for xi in x]
    ans = x_abs[0]
    for xi in x_abs[1:]:
        ans = gcd(ans, xi)
    print(ans)


def __starting_point():
    N, X = list(map(int, input().split()))
    x = [int(i) for i in input().split()]
    solve(N, X, x)

    # # test
    # from random import randint
    # from func import random_str
    # N, X = 10 ** 5, randint(1, 10 ** 9)
    # x = [randint(1, 10 ** 9) for _ in range(N)]
    # solve(N, X, x)


__starting_point()
