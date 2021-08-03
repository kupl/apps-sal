# input = sys.stdin.readline
from bisect import *
from collections import *
from heapq import *
# import functools
# import itertools
# import math

A, B = list(map(int, input().split()))
A -= 1
B -= 1
lst = [["#" if m < 50 else "." for i in range(100)] for m in range(100)]
for h in range(0, 100, 2):
    for w in range(0, 100, 2):
        if A == 0:
            break
        lst[h][w] = "."
        A -= 1

    if A == 0:
        break
for h in range(99, -1, -2):
    for w in range(0, 100, 2):
        if B == 0:
            break
        lst[h][w] = "#"
        B -= 1

    if B == 0:
        break
print((100, 100))
for i in range(100):
    print(("".join(lst[i])))
