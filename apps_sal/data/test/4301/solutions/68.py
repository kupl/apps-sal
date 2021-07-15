import sys
import copy
import math
import itertools
import numpy as np
N = int(input())
A = [int(input()) for c in range(N)]
B = sorted(copy.deepcopy(A),reverse=True)

for i in range(N):
    if A[i] == B[0]:
        print(B[1])
    else:
        print(B[0])
