import sys
import copy
import math
import itertools
import numpy as np

H, W = [int(c) for c in input().split()]
s = [list(input()) for c in range(H)]
a = [[1 for c in range(W)] for d in range(H)]
b = [[0 for c in range(W)] for d in range(H)]

for i in range(H):
    for j in range(W):
        if s[i][j] == "#":
            if i - 1 >= 0:
                if s[i - 1][j] == "#":
                    a[i][j] = 0
            if j - 1 >= 0:
                if s[i][j - 1] == "#":
                    a[i][j] = 0
            if j + 1 < W:
                if s[i][j + 1] == "#":
                    a[i][j] = 0
            if i + 1 < H:
                if s[i + 1][j] == "#":
                    a[i][j] = 0
        else:
            a[i][j] = 0
        if a[i][j] == 1:
            print("No")
            return

print("Yes")
