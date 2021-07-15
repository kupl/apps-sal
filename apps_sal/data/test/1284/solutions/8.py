#!/usr/bin/env python3
import sys
input = sys.stdin.readline

n = int(input())
a = [int(item) for item in input().split()]
total = sum(a)
if n == 1:
    print(total)
    return
val = sum(a[::2])
a.append(a[0])

ans = 0
for a0, a1 in zip(a, a[1:]):
    val = total - val + a0
    ans = max(ans, val)
print(ans)
