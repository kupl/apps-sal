#!/usr/bin/env python3
from collections import deque
import bisect
import sys
input = sys.stdin.readline

n = int(input())
a = [int(item) for item in input().split()]
b = [int(item) for item in input().split()]

c = []
for aa, bb in zip(a, b):
    c.append(aa - bb)

c.sort()
c = deque(c)
ans = 0
while c:
    item = c.popleft()
    val = len(c) - bisect.bisect_right(c, -item)
    ans += val
print(ans)
