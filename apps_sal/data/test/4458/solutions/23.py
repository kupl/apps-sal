import sys
import copy
import math
import itertools
import numpy as np
N = int(input())
P = [int(c) for c in input().split()]
min = P[0]
cnt = 0
for i in range(N):
    if min >= P[i]:
        min = P[i]
        cnt += 1
print(cnt)
