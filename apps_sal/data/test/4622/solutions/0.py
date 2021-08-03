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
a = L()
s = set()
for i in range(n):
    if a[i] in s:
        print("NO")
        return
    s.add(a[i])
print("YES")
