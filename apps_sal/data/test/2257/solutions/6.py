#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

#   = input()
#   = int(input())

#() = (i for i in input().split())
#   = [i for i in input().split()]

(n, x1, y1, x2, y2) = (int(i) for i in input().split())
r1 = []
r2 = []

for i in range(n):
    (x, y) = (int(i) for i in input().split())
    r1.append((x - x1) * (x - x1) + (y - y1) * (y - y1))
    r2.append((x - x2) * (x - x2) + (y - y2) * (y - y2))


start = time.time()

if max(r1) > max(r2):
    (r1, r2) = (r2, r1)

r1s = sorted(list(set(r1)), key=lambda x: -x)

ra2 = 0
ans = r1s[0]
now = 0

while(now < len(r1s) - 1):
    rn2 = ra2
    for i in range(n):
        if r1[i] == r1s[now]:
            if r2[i] > rn2:
                rn2 = r2[i]

    if rn2 + r1s[now + 1] < ans:
        ans = rn2 + r1s[now + 1]

    ra2 = rn2
    now += 1

print(ans)
finish = time.time()
#print(finish - start)
