import sys
import copy
import math
import itertools
import numpy as np
l = [int(c) for c in input().split()]
H = l[0]
W = l[1]
a = [input() for c in range(H)]
print('#' * (W + 2))
for i in range(H):
    print('#' + a[i] + '#')
print('#' * (W + 2))
