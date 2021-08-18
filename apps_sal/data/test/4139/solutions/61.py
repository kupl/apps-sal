import sys
from math import factorial


def comb(n, r):
    return factorial(n) // factorial(r) // factorial(n - r)


def perm(n, r):
    return factorial(n) // factorial(r)


def resultSur97(x):
    return x % (10 ** 9 + 7)


def dfs(s, n):
    if int(s) > n:
        return 0
    if all(s.count(c) > 0 for c in "753"):
        ret = 1
    else:
        ret = 0
    for c in '753':
        ret += dfs(s + c, n)
    return ret


def __starting_point():
    a = int(input())

    print(("{}".format(dfs("0", a))))


__starting_point()
