import sys
import math
import string
import operator
import functools
import fractions
import collections
sys.setrecursionlimit(10**7)
dX = [-1, 1, 0, 0, -1, 1, -1, 1]
dY = [0, 0, -1, 1, 1, -1, -1, 1]
def RI(): return list(map(int, input().split()))
def RS(): return input().rstrip().split()


#################################################
n, k = RI()
if n == k:
    print(-1)
else:
    print(n - k, end=" ")
    for i in range(1, n - k):
        print(i, end=" ")
    for i in range(n - k + 1, n + 1):
        print(i, end=" ")
