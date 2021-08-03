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

a, b = L()
for i in range(10, 1250):
    if int(i * 0.08) == a and int(i * 0.1) == b:
        print(i)
        return
print(-1)
