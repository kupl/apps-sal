from collections import defaultdict as dd
from math import sqrt
import sys
input = sys.stdin.readline
(n, m, k) = list(map(int, input().split()))
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
cou = 0
d1 = dd(int)
for i in range(n):
    if l1[i]:
        cou += 1
    else:
        cc = cou
        for j in range(1, cou + 1):
            d1[j] += cc
            cc -= 1
        cou = 0
cc = cou
for j in range(1, cou + 1):
    d1[j] += cc
    cc -= 1
cou = 0
d2 = dd(int)
cou = 0
for i in range(m):
    if l2[i]:
        cou += 1
    else:
        cc = cou
        for j in range(1, cou + 1):
            d2[j] += cc
            cc -= 1
        cou = 0
cc = cou
for j in range(1, cou + 1):
    d2[j] += cc
    cc -= 1
cou = 0
sk = int(sqrt(k))
su = 0
for i in range(1, sk + 1):
    if k % i == 0:
        su += d1[i] * d2[k // i]
        if i != k // i:
            su += d1[k // i] * d2[i]
print(su)
