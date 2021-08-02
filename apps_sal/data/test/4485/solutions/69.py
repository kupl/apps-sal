# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 02:05:32 2020

@author: liang
"""

N, M = map(int, input().split())
first = list()
second = set()

for i in range(M):
    a, b = map(int, input().split())
    if a == 1:
        first.append(b)
    if b == N:
        second.add(a)

for a in first:
    if a in second:
        print("POSSIBLE")
        break
else:
    print("IMPOSSIBLE")
