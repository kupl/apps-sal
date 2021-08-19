#!/usr/bin/env python3
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = [int(item) for item in input().split()]
    all_same = True
    has_same = False
    for item in a:
        if item != x:
            all_same = False
        if item == x:
            has_same = True
    if all_same:
        print(0)
        continue
    if sum(a) == x * n or has_same:
        print(1)
        continue
    print(2)
