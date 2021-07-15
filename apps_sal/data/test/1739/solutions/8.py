#!/usr/bin/env python3

import sys
import heapq

n, x = list(map(int, sys.stdin.readline().split()))
a = list(map(int, sys.stdin.readline().split()))
s = sum(a)

h = []
for y in a:
    heapq.heappush(h, s - y)

p, cnt = 0, 0

while len(h) > 0:
    z = heapq.heappop(h)
    if p == z:
        cnt += 1
        if cnt == x:
            heapq.heappush(h, p + 1)
            cnt = 0
    else:
        if cnt != 0:
            print(pow(x, min(p, s), 10 ** 9 + 7))
            return
        cnt = 1
        p = z

print(pow(x, min(p, s), 10 ** 9 + 7))

