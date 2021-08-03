#!/usr/bin/env python3
from itertools import combinations
import sys
input = sys.stdin.readline
INF = 10**9

t = int(input())
for i in range(t):
    n = int(input())
    a = [INF] + [int(item) for item in input().split()] + [INF]
    ans = [1]
    l = r = a.index(1)
    max_val = 1
    for i in range(2, n + 1):
        if i == max(max_val, a[l - 1]):
            ans.append(1)
            l -= 1
            max_val = i
        elif i == max(max_val, a[r + 1]):
            ans.append(1)
            r += 1
            max_val = i
        elif a[l - 1] < a[r + 1]:
            ans.append(0)
            max_val = max(max_val, a[l - 1])
            l -= 1
        else:
            ans.append(0)
            max_val = max(max_val, a[r + 1])
            r += 1
    print("".join([str(item) for item in ans]))
