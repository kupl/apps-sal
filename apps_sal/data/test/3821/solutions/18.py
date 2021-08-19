from sys import stdin, stdout
from collections import defaultdict, Counter
from bisect import bisect, bisect_left
import math
from itertools import permutations
I = stdin.readline
n = int(I())
arr = [float(x) for x in I().split()]
arr.sort(reverse=True)
ma = arr[0]
for i in range(1, n):
    now = ma * (1 - arr[i])
    sec = 1
    for j in range(i):
        sec *= 1 - arr[j]
    now += arr[i] * sec
    if now > ma:
        ma = now
    else:
        break
print(ma)
