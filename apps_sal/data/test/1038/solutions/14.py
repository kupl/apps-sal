import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def f(x):
        if x % 2:
            if x == 1:
                return 1
            elif max(0, x - 3) % 4 == 0:
                return 0
            else:
                return 1
        else:
            t = f(x - 1)
            return t ^ x

    a, b = list(map(int, input().split()))

    res = f(b) ^ f(a - 1)
    print(res)


def __starting_point():
    resolve()


__starting_point()
