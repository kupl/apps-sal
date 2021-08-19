# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 16:23:28 2020

@author: liang
"""

N, M = map(int, input().split())
AC_list = [0] * N
WA_list = [0] * N

for i in range(M):
    p, j = input().split()
    p = int(p)
    if j == 'AC':
        AC_list[p - 1] += 1
    else:
        if AC_list[p - 1] == 0:
            WA_list[p - 1] += 1

AC = 0
WA = 0
for i in range(N):
    if AC_list[i] >= 1:
        AC += 1
        WA += WA_list[i]

print(AC, WA)
