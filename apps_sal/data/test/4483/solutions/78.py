import sys
sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    x = int(input())
    a = int(input())
    b = int(input())
    x -= a
    res = x % b
    print(res)


def __starting_point():
    resolve()


__starting_point()
