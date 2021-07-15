from math import sqrt

__author__ = 'Konrad Strack'


def solve():
    r, x1, y1, x2, y2 = [int(x) for x in input().split()]

    d = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    steps = int(d // (2 * r))
    if steps * (2 * r) < d:
        steps += 1

    print(steps)


def __starting_point():
    solve()
__starting_point()
