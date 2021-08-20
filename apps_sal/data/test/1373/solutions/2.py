import collections
import math
import sys
import numpy as np


def N():
    return int(input())


def L():
    return list(map(int, input().split()))


def NL(n):
    return [list(map(int, input().split())) for i in range(n)]


mod = pow(10, 9) + 7
(n, k) = L()
n += 1
l = [i for i in range(n)]
l = np.cumsum(l)
l %= mod
sum = 1
for i in range(k, n):
    sa = l[n - 1] - l[n - 1 - i] - l[i - 1] + 1
    sum += sa
    sum %= mod
print(sum)
