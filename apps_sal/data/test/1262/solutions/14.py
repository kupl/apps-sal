import bisect
import functools
import math
import sys
from collections import defaultdict


def rt(): return map(int, input().split())
def ri(): return int(input())
def rl(): return list(map(int, input().split()))


def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def main():
    n = ri()
    x, y = [0] * n, [0] * n
    for i in range(n):
        x[i], y[i] = rt()
    c = rl()
    k = rl()

    val = c.copy()
    used = [False] * n
    link = [-1] * n
    to_build = []
    for _ in range(n):
        min_index = -1
        min_val = math.inf
        for i in range(n):
            if not used[i] and val[i] < min_val:
                min_index = i
                min_val = val[i]

        used[min_index] = True
        if link[min_index] == -1:
            to_build.append(min_index + 1)
        for i in range(n):
            if not used[i]:
                to_link = (k[i] + k[min_index]) * dist(x[i], y[i], x[min_index], y[min_index])
                if to_link < val[i]:
                    val[i] = to_link
                    link[i] = min_index

    print(sum(val))
    print(len(to_build))
    print(*to_build)
    print(len([x for x in link if x > -1]))
    for i in range(n):
        if link[i] > -1:
            print(i + 1, link[i] + 1)


def __starting_point():
    main()


__starting_point()
