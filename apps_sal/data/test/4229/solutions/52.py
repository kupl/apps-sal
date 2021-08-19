import collections
import math
import sys


def N():
    return int(input())


def L():
    return list(map(int, input().split()))


def NL(n):
    return [list(map(int, input().split())) for i in range(n)]


mod = pow(10, 9) + 7

#import numpy as np

n = N()
cnt = 0
for i in range(n + 1):
    if i % 3 != 0 and i % 5 != 0:
        cnt += i
print(cnt)
