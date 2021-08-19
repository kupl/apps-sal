#!/bin/python3
import sys
import math
n = int(input())
a = list(map(int, input().split()))
even = 0
odds = []
for i in range(n):
    if a[i] % 2 == 0 and a[i] > 0:
        even += a[i]
    elif a[i] % 2 == 1:
        odds.append(-a[i])
odds.sort()
maxsum = -odds[0]
i = 1
cursum = -odds[0]
while i < len(odds):
    cursum += -(odds[i])
    i += 1
    if i >= len(odds):
        break
    cursum += -(odds[i])
    i += 1
    maxsum = max(maxsum, cursum)
print(maxsum + even)
