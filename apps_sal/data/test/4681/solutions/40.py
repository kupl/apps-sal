import sys
import copy
import math
import itertools
import numpy as np
N = int(input())
L = [2, 1]
for i in range(N - 1):
    L.append(L[i] + L[i + 1])

print(L[N])
