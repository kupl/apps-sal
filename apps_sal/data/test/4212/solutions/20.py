# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 23:43:13 2020

@author: liang
"""

N, M, Q = map(int, input().split())

A = list()
lis = list()
ans = 0


def make_list(n, m):
    if n == N:
        A.append(lis.copy())
        return
    for i in range(m, M + 1):
        lis.append(i)
        make_list(n + 1, i)
        lis.pop()


make_list(0, 1)
# print(A)

calc = [list(map(int, input().split())) for _ in range(Q)]

for a in A:
    tmp = 0
    for c in calc:
        if a[c[1] - 1] - a[c[0] - 1] == c[2]:
            tmp += c[3]
    if tmp > ans:
        ans = tmp

print(ans)
