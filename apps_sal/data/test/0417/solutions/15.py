#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, x, d = [int(item) for item in input().split()]

if d == 0:
    if x == 0:
        print(1)
    else:
        print(n+1)
    return

range_in_kXmodD = dict() 
for i in range(0, n+1):
    kXmodD = i * x % d
    start = (i * x) // d + i * (i - 1) // 2
    end = (i * x) // d + i * (n - i + n - 1) // 2 + 1
    if kXmodD not in range_in_kXmodD:
        range_in_kXmodD[kXmodD] = []
    range_in_kXmodD[kXmodD].append((start, 1))
    range_in_kXmodD[kXmodD].append((end, -1))

ans = 0
for key in range_in_kXmodD.keys():
    range_in_kXmodD[key].sort()
    ret = 0
    cnt = 0
    prev = None 
    for val, c in range_in_kXmodD[key]:
        if prev != None and cnt > 0:
            ret += val - prev
        cnt += c
        prev = val
    ans += ret

print(ans)
