#!/usr/bin/env python3
from sys import stdin, stdout


def ri():
    return list(map(int, input().split()))


w = 15
adding = [(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)]


def fill(x, y, dir, depth):
    for i in range(t[depth]):
        x += adding[dir][0]
        y += adding[dir][1]
        v[x][y] = 1


def dfs(x, y, dir, depth):
    if depth == n:
        return
    #print(T, dir, depth)
    if (dir, depth) in T[x][y]:
        # print("found")
        #print(T, dir, depth)
        return
    fill(x, y, dir, depth)
    ndepth = depth + 1
    nx = x + adding[dir][0] * t[depth]
    ny = y + adding[dir][1] * t[depth]
    ndir = (dir + 1) % 8
    dfs(nx, ny, ndir, ndepth)
    ndir = (8 + dir - 1) % 8
    dfs(nx, ny, ndir, ndepth)
    T[x][y].add(tuple((dir, depth)))


n = int(input())
t = list(ri())

v = [[0 for i in range(n * w)] for j in range(n * w)]

T = [[set() for i in range(n * w)] for j in range(n * w)]

# x, y, dir, depth
dfs(n * w // 2, n * w // 2, 0, 0)

ans = 0
for i in range(n * w):
    for j in range(n * w):
        if v[i][j]:
            ans += 1

print(ans)
