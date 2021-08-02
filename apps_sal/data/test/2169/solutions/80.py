import sys
import math
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    H, W, D = NMI()
    grid = [NLI() for i in range(H)]
    Q = NI()
    querys = [NLI() for i in range(Q)]

    point = [[-1, -1] for _ in range(H * W + 1)]
    for h in range(H):
        for w in range(W):
            a = grid[h][w]
            point[a] = [h, w]

    cost_S = [0] * (H * W + 1)
    for c in range(H * W + 1):
        if c <= D:
            continue

        cost_S[c] = cost_S[c - D] + abs(point[c][0] - point[c - D][0]) + abs(point[c][1] - point[c - D][1])

    for query in querys:
        l, r = query
        print(cost_S[r] - cost_S[l])


def __starting_point():
    main()


__starting_point()
