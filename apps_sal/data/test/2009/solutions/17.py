# -*- coding: utf-8 -*-
# @Time    : 2019/2/25 0:05
# @Author  : LunaFire
# @Email   : gilgemesh2012@gmail.com
# @File    : C. Connect.py

from collections import deque


def floodfill(x, y, grid, mark):
    if grid[x][y] != '0':
        return

    n = len(grid)
    queue = deque()
    queue.append((x, y))

    while queue:
        cx, cy = queue[0]
        queue.popleft()
        if grid[cx][cy] == mark:
            continue
        grid[cx][cy] = mark

        for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + d[0], cy + d[1]
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == '0':
                queue.append((nx, ny))


def main():
    n = int(input())
    r1, c1 = list(map(int, input().split()))
    r2, c2 = list(map(int, input().split()))
    r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1

    grid = []
    for _ in range(n):
        grid.append(list(input()))

    floodfill(r1, c1, grid, '*')
    floodfill(r2, c2, grid, '-')
    # for i in range(n):
    #     print(grid[i])

    if grid[r1][c1] == grid[r2][c2]:
        print(0)
    else:
        pos1, pos2 = [], []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == '*':
                    pos1.append((i, j))
                elif grid[i][j] == '-':
                    pos2.append((i, j))

        ret = float('inf')
        # print(len(pos1))
        # print(len(pos2))
        for rs, cs in pos1:
            for rt, ct in pos2:
                ret = min(ret, (rt - rs) ** 2 + (ct - cs) ** 2)
        print(int(ret))


def __starting_point():
    main()


__starting_point()
