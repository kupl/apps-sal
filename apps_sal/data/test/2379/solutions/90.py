import sys
import math
import numpy as np
import itertools
(n, k, c) = (int(i) for i in input().split())
m = list(input())
l = [-1] * n
r = [-1] * n
a = 0
b = c
for i in range(n):
    if b >= c and m[i] == 'o':
        b = 0
        l[a] = i
        a += 1
    else:
        b += 1
    if a == k:
        break
a = k - 1
b = c
for i in range(n - 1, -1, -1):
    if b >= c and m[i] == 'o':
        b = 0
        r[a] = i
        a -= 1
    else:
        b += 1
    if a == k:
        break
answer = 0
for i in range(n):
    if l[i] == r[i] and l[i] >= 0:
        print(l[i] + 1)
