import sys
import copy
import math
import itertools
import numpy as np

N = int(input())
S = input()
x = 0
max = 0
for i in range(N):
    if S[i] == "I":
        x += 1
    elif S[i] == "D":
        x -= 1

    if max < x:
        max = x

print(max)
