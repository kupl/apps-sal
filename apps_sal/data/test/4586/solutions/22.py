#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n = str(int(input()))

flag = False
if n[0] == n[1] and n[1] == n[2]:
    flag = True
if n[1] == n[2] and n[3] == n[2]:
    flag = True

if flag:
    print("Yes")
else:
    print("No")
