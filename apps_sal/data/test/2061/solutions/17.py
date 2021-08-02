#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys


def delete(j, m):
    nonlocal a
    i = 0
    while(i < len(oz[j])):
        w, b = oz[j][i], oz[j][i + 1]
        i += 2
        a[w][b] = '*'


def poi(i, j, k):
    visited[i][j] = True
    oz[k] += i, j
    ozsi[k] += 1
    if (j - 1) >= 0 and a[i][j - 1] == '.' and not visited[i][j - 1]:
        poi(i, j - 1, k)
    if (j + 1) <= (m + 1) and a[i][j + 1] == '.' and not visited[i][j + 1]:
        poi(i, j + 1, k)
    if (i - 1) >= 0 and a[i - 1][j] == '.' and not visited[i - 1][j]:
        poi(i - 1, j, k)
    if (i + 1) <= (n + 1) and a[i + 1][j] == '.' and not visited[i + 1][j]:
        poi(i + 1, j, k)


n, m, vb = map(int, input().split())
a = []
oz = []
ozsi = []
visited = [[False for r in range(m + 2)] for t in range(n + 2)]
a.append(['.'] * (m + 2))
sys.setrecursionlimit(3000)
for i in range(n):
    s = '.' + input() + '.'
    a.append([str(x) for x in s])
k = 0
a.append(['.'] * (m + 2))
for i in range(0, n + 2):
    for j in range(0, m + 2):
        if a[i][j] == '.':
            if not visited[i][j]:
                ozsi.append(0)
                oz.append([])
                poi(i, j, k)
                k += 1
t = len(ozsi) - vb - 1
e = 0
for i in range(t):
    min = 10**10
    minj = 0
    for j in range(1, len(ozsi)):
        if ozsi[j] < min:
            min = ozsi[j]
            minj = j
    e += min
    delete(minj, min)
    ozsi[minj] = 10**10
print(e)
for i in range(1, n + 1):
    for j in range(1, m + 1):
        print(a[i][j], end='')
    print()
