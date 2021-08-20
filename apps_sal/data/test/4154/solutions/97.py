import sys
import copy
import math
import itertools
import numpy as np
l = [int(c) for c in input().split()]
N = l[0]
M = l[1]
LR = [list(map(int, input().split())) for c in range(M)]
small = 0
large = N
for i in range(M):
    if small < LR[i][0]:
        small = LR[i][0]
    if large > LR[i][1]:
        large = LR[i][1]
if small <= large:
    print(large - small + 1)
else:
    print(0)
