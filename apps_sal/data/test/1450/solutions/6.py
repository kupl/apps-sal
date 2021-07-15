import time
from copy import deepcopy
import itertools
from bisect import bisect_left
from bisect import bisect_right
import math
from collections import deque
from collections import Counter


def read():
    return int(input())


def readmap():
    return map(int, input().split())


def readlist():
    return list(map(int, input().split()))


S = list(map(int, list(input())))
num1 = S.count(1)
for i in range(len(S)):
    if S[i] == 2:
        index = i
        break
    index = len(S)

ans = []
for i in range(len(S)):
    if i == index:
        ans += [1] * num1
    if S[i] != 1:
        ans.append(S[i])

if index == len(S):
    ans += [1] * num1

print("".join(list(map(str, ans))))
