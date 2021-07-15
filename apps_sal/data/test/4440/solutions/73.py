import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    l = int(input())
    res = pow(l / 3, 3)
    print(res)


def __starting_point():
    resolve()

__starting_point()
