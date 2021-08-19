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
c = [[0] * 10 for i in range(10)]
for i in range(1, n + 1):
    h = int(str(i)[0])
    t = int(str(i)[-1])
    c[h][t] += 1
sum = 0
for i in range(1, 10):
    for j in range(1, 10):
        sum += c[i][j] * c[j][i]
print(sum)
