#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	C
# CreatedDate:  2020-06-27 11:11:46 +0900
# LastModified: 2020-10-01 00:51:09 +0900
#


import os
import sys
import numpy as np
# import pandas as pd


def dfs(visited, maze, h, w):
    visited[h, w] = -1
    if maze[h, w + 1] == 1 and visited[h, w + 1] == 1:
        dfs(visited, maze, h, w + 1)
    if maze[h, w - 1] == 1 and visited[h, w - 1] == 1:
        dfs(visited, maze, h, w - 1)
    if maze[h + 1, w] == 1 and visited[h + 1, w] == 1:
        dfs(visited, maze, h + 1, w)
    if maze[h - 1, w] == 1 and visited[h - 1, w] == 1:
        dfs(visited, maze, h - 1, w)


def check_maze(maze, h, w):
    if maze[h, w + 1] == 1:
        return 1
    elif maze[h, w - 1] == 1:
        return 1
    elif maze[h + 1, w] == 1:
        return 1
    elif maze[h - 1, w] == 1:
        return 1
    else:
        return 0


def main():
    H, W = list(map(int, input().split()))
    maze = []
    for _ in range(H):
        S = input()
        S = [1 if s == '#' else 0 for s in S]
        maze.append(S)
    maze = np.array(maze)
    maze = np.pad(maze, [(1, 1), (1, 1)])
    visited = np.copy(maze)
    for h in range(1, H + 1):
        for w in range(1, W + 1):
            if maze[h, w] == 1:
                flag = check_maze(maze, h, w)
                if flag == 0:
                    print("No")
                    return
    print("Yes")


def __starting_point():
    main()


__starting_point()
