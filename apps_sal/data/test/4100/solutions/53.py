import sys
import copy
import math
import itertools
import numpy as np
l = [int(c) for c in input().split()]
N = l[0]
K = l[1]
Q = l[2]
A = [int(input()) for c in range(Q)]

S = [K] * N

for i in range(Q):
    S[A[i] - 1] += 1

for i in range(N):
    if S[i] - Q > 0:
        print("Yes")
    else:
        print("No")
