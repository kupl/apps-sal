import sys
# import math
# import bisect
# import numpy as np
# from decimal import Decimal
# from numba import njit, i8, u1, b1 #JIT compiler
# from itertools import combinations, product
# from collections import Counter, deque, defaultdict

# sys.setrecursionlimit(10 ** 6)
MOD = 10 ** 9 + 7
INF = 10 ** 9
PI = 3.14159265358979323846


def read_str(): return sys.stdin.readline().strip()
def read_int(): return int(sys.stdin.readline().strip())
def read_ints(): return map(int, sys.stdin.readline().strip().split())
def read_ints2(x): return map(lambda num: int(num) - x, sys.stdin.readline().strip().split())
def read_str_list(): return list(sys.stdin.readline().strip().split())
def read_int_list(): return list(map(int, sys.stdin.readline().strip().split()))
def GCD(a: int, b: int) -> int: return b if a % b == 0 else GCD(b, a % b)
def LCM(a: int, b: int) -> int: return (a * b) // GCD(a, b)


def search(topx, topy, botx, boty, grid):
    ret = grid[boty][botx]
    if topx > 0:
        ret -= grid[boty][topx - 1]
    if topy > 0:
        ret -= grid[topy - 1][botx]
    if topx > 0 and topy > 0:
        ret += grid[topy - 1][topx - 1]
    return ret


def Main():
    H, W, K = read_ints()
    chocolate = [list(read_str()) for _ in range(H)]

    grid = [[0] * W for _ in range(H)]
    for h in range(H):
        for w in range(W):
            if chocolate[h][w] == '1':
                grid[h][w] += 1
            if w > 0:
                grid[h][w] += grid[h][w - 1]
            if h > 0:
                grid[h][w] += grid[h - 1][w]
            if h > 0 and w > 0:
                grid[h][w] -= grid[h - 1][w - 1]

    ans = INF
    for bit in range(1 << ~-H):
        cnt = 0
        cut = []
        for h in range(~-H):
            if bit >> h & 1:
                cnt += 1
                cut.append(h)
        cut.append(~-H)

        white = [0] * len(cut)
        topx = 0
        flag = False
        for w in range(~-W):
            topy = 0
            for i in range(len(cut)):
                if search(topx, topy, w, cut[i], grid) > K:
                    flag = True
                    break
                white[i] = search(topx, topy, w + 1, cut[i], grid)
                topy = cut[i] + 1
            if flag:
                break
            for x in white:
                if x <= K:
                    continue
                topx = w + 1
                cnt += 1
                break
        if not flag:
            ans = min(ans, cnt)
    print(ans)


def __starting_point():
    Main()


__starting_point()
