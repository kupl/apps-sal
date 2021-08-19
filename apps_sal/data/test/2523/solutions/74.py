#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

s = list(str(input()))

max_ = len(s)
for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        left = i + 1
        right = len(s) - left
        # print(left, right)
        tmp = max(left, right)

        max_ = min(max_, tmp)
print(max_)
