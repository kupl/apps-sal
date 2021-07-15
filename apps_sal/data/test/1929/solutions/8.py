#!/usr/bin/env python

from sys import stdin

n, t, c = list(map(int, stdin.readline().split()))
cnt = 0
ct = 0
for i in map(int, stdin.readline().split()):
    if i <= t:
        ct = ct + 1
    else:
        if ct >= c:
            cnt = cnt + ct - c + 1
        ct = 0
if ct >= c:
    cnt = cnt + ct - c + 1
print(cnt)

