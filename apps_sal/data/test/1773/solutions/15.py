#!/usr/bin/env python
# -*- coding: utf-8 -*-

n = int(input())
Left = []
Right = []
for i in range(n):
    t = list(map(int, input().split()))
    if t[0] < 0:
        Left.append(t)
    if t[0] > 0:
        Right.append(t)

num = min(len(Left), len(Right))

Right = [a[1] for a in sorted(Right, key=lambda x:x[0])]
Left = [a[1] for a in sorted(Left, key=lambda x:-x[0])]

if len(Left) < len(Right):
    ans = sum(Right[:num + 1] + Left[:num])
elif len(Left) > len(Right):
    ans = sum(Right[:num] + Left[:num + 1])
else:
    ans = sum(Right[:num] + Left[:num])
print(ans)
