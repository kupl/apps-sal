import sys
import math
from collections import deque
from collections import Counter
sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def NI():
    return int(input())


def NMI():
    return map(int, input().split())


def NLI():
    return list(NMI())


def SI():
    return input()


def main():
    (H, W, N) = NMI()
    grid = {}
    for i in range(N):
        (a, b) = NMI()
        for t in range(-2, 1):
            for k in range(-2, 1):
                if a + t < 1 or b + k < 1:
                    continue
                if a + t >= H - 1 or b + k >= W - 1:
                    continue
                point = (a + t) * 10 ** 10 + b + k
                grid[point] = grid.get(point, 0) + 1
    c = Counter(grid.values())
    for i in range(10):
        if i == 0:
            print((H - 2) * (W - 2) - sum(c.values()))
        else:
            print(c.get(i, 0))


def __starting_point():
    main()


__starting_point()
