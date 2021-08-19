import os
import sys
import re
import math
N = int(input())
X = [int(n) for n in input().split()]
d = [i ** 2 for i in range(101)]
min_v = 100 ** 2 * 100
for i in range(1, 101):
    min_v = min(min_v, sum((d[abs(x - i)] for x in X)))
print(min_v)
