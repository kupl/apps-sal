#!/usr/bin/env python3
import sys
import os

N = int(input())
s = set()
v = list(map(int, input().split()))
ans = 0

for i in range(0, 2 * N):
    if v[i] in s:
        s.remove(v[i])
    else:
        s.add(v[i])
    ans = max(ans, len(s))

print(ans)
