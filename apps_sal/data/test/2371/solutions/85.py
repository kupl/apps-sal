#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n, z, w = list(map(int, input().split()))
a = list(map(int, input().split()))

if n == 1:
    ans = abs(a[0]-w)
    print(ans)
    return

ans1 = abs(a[-2]-a[-1])
ans2 = abs(a[-1]-w)
# print(ans1, ans2)
print((max(ans1, ans2)))

