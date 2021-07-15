#!/usr/bin/env python3
import sys
input = sys.stdin.readline

s = input().rstrip()
n = len(s)
l = 0; r = n - 1
ans = []
while r - l > 0:
    while l != r and s[l] != "(":
        l += 1
    while r != l and s[r] != ")":
        r -= 1
    if l != r:
        ans.append(l+1)
        l += 1
        ans.append(r+1)
        r -= 1
if len(ans) == 0:
    print(0)
    return
else:
    print(1)
    print(len(ans))
    ans.sort()
    print(*ans)

