#!/usr/bin/env python3
import sys
input = sys.stdin.readline

n = int(input())
s = list(input().rstrip())
t = list(input().rstrip())

if s.count("1") != t.count("1"):
    print(-1)
    return

ns = []
for si, ti in zip(s, t):
    if si != ti:
        ns.append(si)
ns = ns + ns
d = 0
ans = 0
for item in ns:
    if item == "1":
        d += 1
    else:
        d -= 1
        if d < 0:
            d = 0
    ans = max(ans, d)

print(ans)
