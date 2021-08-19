#!/usr/bin/env python3

n = int(input())
s = set(map(str, input().split()))

if len(s) == 4:
    print("Four")
else:
    print("Three")
