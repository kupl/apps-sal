# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 02:34:35 2020

@author: liang
"""

N = int(input())
S = input()

count = 1
for i in range(N - 1):
    if S[i] != S[i + 1]:
        count += 1
print(count)
