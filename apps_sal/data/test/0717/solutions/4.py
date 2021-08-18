import collections
import random
import sys


n = int(input())
day = 0
for i in range(n):
    s, d = list(map(int, input().split()))
    day = max(day + 1, s)
    if (day - s) % d != 0:
        day += d - (day - s) % d
print(day)
