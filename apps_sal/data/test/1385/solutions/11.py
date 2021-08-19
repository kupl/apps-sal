import re
import sys
import math
import string
import operator
import functools
import fractions
import collections
import os
sys.setrecursionlimit(10**7)
dX = [-1, 1, 0, 0, -1, 1, -1, 1]
dY = [0, 0, -1, 1, 1, -1, -1, 1]
def RI(): return list(map(int, input().split()))
def RS(): return input().rstrip().split()


mod = 1e9 + 7
#################################################
s = input() + ' '
ans = []
i, j = 0, -1
while i < len(s):
    if s[i] == ' ':
        if j != -1:
            ans.append(s[j:i])
        j = -1
    elif s[i] == "\"":
        j = i + 1
        i += 1
        while s[i] != "\"":
            i += 1
        ans.append(s[j:i])
        j = -1
    else:
        if j == -1:
            j = i
    i += 1
for i in ans:
    print('<' + i + '>')
