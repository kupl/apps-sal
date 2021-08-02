from collections import defaultdict
from sys import stdin

input = stdin.readline


def solve():

    a, b, x, y = map(int, input().split())
    d = abs(a - b)
    if d == 0:
        print(x)
        return

    elif a < b:
        print(d * y + x if y <= 2 * x else d * 2 * x + x)
        return
    else:
        print((d - 1) * y + x if y <= 2 * x else d * x * 2 - x)


def __starting_point():
    solve()


__starting_point()
