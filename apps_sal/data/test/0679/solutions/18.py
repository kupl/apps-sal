from copy import deepcopy
import itertools
from bisect import bisect_left
from bisect import bisect_right
import math


def read():
    return int(input())


def readmap():
    return map(int, input().split())


def readlist():
    return list(map(int, input().split()))


S = input()
if len(S) <= 2:
    print('No')
    quit()
for i in range(1, len(S) - 1):
    if S[i - 1] != '.' and S[i] != '.' and (S[i + 1] != '.'):
        if S[i - 1] != S[i] and S[i] != S[i + 1] and (S[i - 1] != S[i + 1]):
            print('Yes')
            quit()
print('No')
