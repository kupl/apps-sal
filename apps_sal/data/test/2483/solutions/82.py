import sys
from collections import *
import heapq
import math
import bisect
import copy
from itertools import permutations, accumulate, combinations, product


def input():
    return sys.stdin.readline()[:-1]


def ruiseki(lst):
    return [0] + list(accumulate(lst))


mod = pow(10, 9) + 7
al = [chr(ord('a') + i) for i in range(26)]
direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]

n, c = map(int, input().split())
stc = [list(map(int, input().split())) for i in range(n)]
stc.sort()
lst = [0] * c
for i in range(n):
    s, t, ctmp = stc[i]
    for j in range(c):
        if lst[j] == 0:
            lst[j] = stc[i]
            break
        else:
            if lst[j][2] == ctmp:
                lst[j] = stc[i]
                break
            elif lst[j][1] < s:
                lst[j] = stc[i]
                break
ans = 0
for i in range(c):
    if lst[i] != 0:
        ans += 1
print(ans)
