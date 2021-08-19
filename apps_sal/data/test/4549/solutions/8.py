# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 10:13:51 2020

@author: liang
"""
H, W = map(int, input().split())
flag = True
field = [input() for i in range(H)]

for i in range(H):
    for j in range(W):
        if field[i][j] == "#":
            tmp = False
            if i - 1 >= 0 and field[i - 1][j] == "#":
                tmp = True
            if i + 1 < H and field[i + 1][j] == "#":
                tmp = True
            if j - 1 >= 0 and field[i][j - 1] == "#":
                tmp = True
            if j + 1 < W and field[i][j + 1] == "#":
                tmp = True
            if tmp == False:
                flag = False

if flag:
    print("Yes")
else:
    print("No")
