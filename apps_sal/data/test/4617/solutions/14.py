#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

c1 = list(str(input()))
c2 = list(reversed(str(input())))

if c1 == c2:
    print("YES")
else:
    print("NO")
