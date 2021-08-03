#!/usr/bin/env python
# -*- coding: utf-8 -*-

n, m = list(map(int, input().split()))
S = input()
char = {chr(i): chr(i) for i in range(ord('a'), ord('z') + 1)}
keys = list(char.keys())

for i in range(m):
    x, y = input().split()
    for c in keys:
        if char[c] == x:
            char[c] = y
        elif char[c] == y:
            char[c] = x

ans = []
for c in list(S):
    ans.append(char[c])
print(''.join(ans))
