# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 01:17:00 2020

@author: liang
"""

S = input()
K = int(input())

#count = 0
for i in range(len(S)):
    if S[i] != '1':
        break
# print("i",i)

if K < i + 1:
    print((1))
    # print("A")
else:
    print((S[i]))
    # print("B")
