import sys
from itertools import permutations

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, c = list(map(int, input().split()))
    D = [list(map(int, input().split())) for _ in range(c)]
    grid = [list(map(int, input().split())) for _ in range(n)]

    col_cnt = [[0] * c for _ in range(3)]
    for i in range(n):
        for j in range(n):
            col = grid[i][j] - 1
            col_cnt[(i + j + 2) % 3][col] += 1

    res = f_inf
    for pattern in permutations(list(range(c)), 3):
        cost = 0
        for idx, col in enumerate(pattern):
            for k in range(c):
                cnt = col_cnt[idx][k]
                cost += D[k][col] * cnt
        res = min(res, cost)
    print(res)


def __starting_point():
    resolve()

__starting_point()
