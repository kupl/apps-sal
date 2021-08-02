import sys
import copy
import math
import itertools
import numpy as np
l = [int(c) for c in input().split()]
A = l[0]
B = l[1]
cnt = 0
for i in range(A, B + 1):
    if str(i)[0] == str(i)[4] and str(i)[1] == str(i)[3]:
        cnt += 1
print(cnt)
