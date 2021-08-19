import string
from collections import Counter, deque
import itertools
import sys
import math
from math import gcd, pi, sqrt
INF = float('inf')
sys.setrecursionlimit(10 ** 6)


def i_input():
    return int(input())


def i_map():
    return list(map(int, input().split()))


def i_list():
    return list(i_map())


def i_row(N):
    return [i_input() for _ in range(N)]


def i_row_list(N):
    return [i_list() for _ in range(N)]


def s_input():
    return input()


def s_map():
    return input().split()


def s_list():
    return list(s_map())


def s_row(N):
    return [s_input for _ in range(N)]


def s_row_str(N):
    return [s_list() for _ in range(N)]


def s_row_list(N):
    return [list(s_input()) for _ in range(N)]


def main():
    (H, W) = i_map()
    dy_dx = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    rc = [input() for i in range(H)]
    ans = 0
    for sy in range(H):
        for sx in range(W):
            if rc[sy][sx] == '#':
                continue
            dist = [[-1 for _ in range(W)] for _ in range(H)]
            dist[sy][sx] = 0
            d = deque()
            d.append([sx, sy])
            while d:
                (nx, ny) = d.popleft()
                for (dy, dx) in dy_dx:
                    (y, x) = (ny + dy, nx + dx)
                    if 0 <= y < H and 0 <= x < W and (rc[y][x] != '#') and (dist[y][x] == -1):
                        dist[y][x] = dist[ny][nx] + 1
                        d.append([x, y])
            ans = max(ans, max(list(itertools.chain.from_iterable(dist))))
    print(ans)


def __starting_point():
    main()


__starting_point()
