#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n = int(input())

fx = sum([int(i) for i in str(n)])


if n % fx == 0:
    print("Yes")
else:
    print("No")
