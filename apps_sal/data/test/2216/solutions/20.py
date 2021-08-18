import collections
import itertools
import fractions
import functools
import heapq
import math
import queue


def solve():
    n, m, k = map(int, input().split())

    cells = []
    for i in range(n):
        if i % 2 == 0:
            for j in range(m):
                cells.append((i + 1, j + 1))
        else:
            for j in range(m, 0, -1):
                cells.append((i + 1, j))

    for _ in range(k - 1):
        print(2, *cells[-1], *cells[-2])
        cells.pop()
        cells.pop()

    print(len(cells), end=' ')
    for c in cells:
        print(*c, end=' ')
    print()


def __starting_point():
    solve()


__starting_point()
