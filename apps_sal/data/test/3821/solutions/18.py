from sys import stdin, stdout
from collections import defaultdict, Counter
from bisect import bisect, bisect_left
import math
from itertools import permutations

#stdin = open('input.txt','r')
I = stdin.readline


n = int(I())
arr = [float(x) for x in I().split()]

arr.sort(reverse=True)
ma = arr[0]
# print(ma)
for i in range(1, n):
    now = ma * (1 - arr[i])
    # print(now)
    sec = 1
    for j in range(i):
        sec *= (1 - arr[j])
   # print(sec*arr[i],sec,arr[i])
    now += (arr[i] * sec)
    # print(ma,now)
    if(now > ma):
        ma = now
    else:
        break

print(ma)
