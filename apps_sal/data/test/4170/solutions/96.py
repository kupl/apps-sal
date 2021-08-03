import sys
import copy
import math
import itertools
import numpy as np
N = int(input())
H = [int(c) for c in input().split()]
max = 0
cnt = 0
for i in range(N - 1):
    if H[i] >= H[i + 1]:
        cnt += 1
        if max < cnt:
            max = cnt
    else:
        cnt = 0
print(max)
