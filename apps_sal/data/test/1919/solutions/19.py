import re
import sys
import string
import operator
import functools
import fractions
import collections
sys.setrecursionlimit(10**7)
dX = [-1, 1, 0, 0, -1, 1, -1, 1]
dY = [0, 0, -1, 1, 1, -1, -1, 1]
RI = lambda x=' ': list(map(int, input().split(x)))
RS = lambda x=' ': input().rstrip().split(x)
mod = int(1e9 + 7)
eps = 1e-6
#################################################
n = RI()[0]
print(2 - (n & 1))
