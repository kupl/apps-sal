#!/usr/bin/env python3
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(item) for item in input().split()]
    ok = False
    for i in range(n - 2):
        for j in range(i + 2, n):
            if a[i] == a[j]:
                ok = True
    if ok:
        print("YES")
    else:
        print("NO")
