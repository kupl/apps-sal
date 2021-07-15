#!/usr/bin/env python3
from collections import Counter
import sys
sys.setrecursionlimit(10**6)


n = int(input())
a = list(map(int, input().split()))

c = Counter(a)

ans = 0
for i in sorted(c.keys()):
    if c[i] < i:
        ans += c[i]
    elif c[i] == i:
        continue
    elif c[i] > i:
        ans += c[i]-i
print(ans)

