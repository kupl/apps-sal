#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kanari
# @Date:   2015-02-08 01:11:21
# @Last Modified by:   kanari
# @Last Modified time: 2015-02-08 01:29:15
[n, m] = map(int, input().split())
a = [0 for i in range(0, n + 1)]
fac = [1]
for i in range(1, n + 1):
    #   fac.append(fac[i - 1] * i)
    fac.append(fac[i - 1] * 2)


def dfs(x, l, r, m):
    if l == r:
        a[l] = x
        return
    elif m <= fac[n - x - 1]:
        a[l] = x
        dfs(x + 1, l + 1, r, m)
    else:
        a[r] = x
        dfs(x + 1, l, r - 1, m - fac[n - x - 1])


dfs(1, 1, n, m)
for i in range(1, n + 1):
    print(a[i], end='')
    if i == n:
        print('\n', end='')
    else:
        print(' ', end='')
