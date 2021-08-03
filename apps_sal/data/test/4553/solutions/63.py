#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

a, b = list(map(int, input().split()))
s = str(input())

x = s.split("-")

if len(x[0]) == a and len(x[1]) == b:
    print("Yes")
else:
    print("No")
