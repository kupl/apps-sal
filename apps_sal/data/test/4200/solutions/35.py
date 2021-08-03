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

n, m = L()
a = L()
h = sum(a) / (4 * m)

a.sort(reverse=True)
for i in range(m):
    if a[i] < h:
        print("No")
        return

print("Yes")
