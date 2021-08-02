#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

s = list(str(input()))

ans = [1 if i == "1" else 0 for i in s]

print((sum(ans)))
