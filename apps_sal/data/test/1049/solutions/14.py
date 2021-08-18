import sys
import math
n, m = map(int, input().split())
z = [0] * m
for i in range(m):
    s = input()
    if '0' in s:
        z[i] = 1
z.append(0)
max_ = 0
now = 0
for i in range(m + 1):
    if z[i] == 0:
        max_ = max(max_, now)
        now = 0
    else:
        now += 1
print(max_)
