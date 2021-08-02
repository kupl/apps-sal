'''input
3
1 3
3 1
010
101
010
'''
import sys
from collections import defaultdict as dd
from itertools import permutations as pp
from itertools import combinations as cc
from collections import Counter as ccd
from random import randint as rd
from bisect import bisect_left as bl
import heapq
mod = 10**9 + 7


def ri(flag=0):
    if flag == 0:
        return [int(i) for i in sys.stdin.readline().split()]
    else:
        return int(sys.stdin.readline())


def valid(i, j):
    if i < 0 or i >= n:
        return 0
    if j < 0 or j >= n:
        return 0
    # print(i,j,mat)
    if vis[i][j] == 1 or mat[i][j] == "1":
        return 0
    return 1


dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(i, j):
    one = [(i, j)]
    vis[i][j] = 1
    s = [(i, j)]
    while s:
        x, y = s.pop(-1)
        for k in range(4):
            if valid(x + dx[k], y + dy[k]):
                vis[x + dx[k]][y + dy[k]] = 1
                s.append((x + dx[k], y + dy[k]))
                one.append((x + dx[k], y + dy[k]))
    return one


n = ri(1)
x1, y1 = [int(i) - 1 for i in input().split()]
x2, y2 = [int(i) - 1 for i in input().split()]

mat = []
vis = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    mat.append(list(input()))

one = bfs(x1, y1)
two = bfs(x2, y2)

ans = 999999999999

for i, j in one:
    for p, q in two:
        ans = min(ans, (i - p)**2 + (j - q)**2)
print(ans)
