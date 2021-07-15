#!/bin/python3
import sys
n = int(input())
a = list(map(int, input().split()))
a = sorted(a)
for i in range(0,n-2):
    if a[i] + a[i + 1] > a[i+2]:
        print("YES")
        return
print("NO")
