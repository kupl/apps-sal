import numpy as np
(H, W) = map(int, input().split())
a = [''] * H
for i in range(H):
    a[i] = input()
h_flag = [0] * H
w_flag = [0] * W
for iHeight in range(H):
    for jWidth in range(W):
        if a[iHeight][jWidth] == '#':
            h_flag[iHeight] = 1
            w_flag[jWidth] = 1
for iHeight in range(H):
    if h_flag[iHeight] == 1:
        for jWidth in range(W):
            if w_flag[jWidth] == 1:
                print(a[iHeight][jWidth], end='')
        print()
