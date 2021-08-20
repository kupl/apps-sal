import sys
import math
from collections import deque
from itertools import permutations
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
    (N, C) = NMI()
    D = [NLI() for _ in range(C)]
    grid = [list(map(lambda x: int(x) - 1, NMI())) for _ in range(N)]
    grid_mod = [{i: 0 for i in range(C)} for _ in range(3)]
    for h in range(N):
        for w in range(N):
            t = (h + w) % 3
            grid_mod[t][grid[h][w]] += 1
    ans = 10 ** 10
    for colors in permutations(range(C), 3):
        diff = 0
        for i in range(3):
            for (c, n) in grid_mod[i].items():
                diff += D[c][colors[i]] * n
        ans = min(ans, diff)
    print(ans)


def __starting_point():
    main()


__starting_point()
