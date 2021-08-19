#!/usr/bin/env python3

n = int(input())
s = input()

p, w = False, False
x, y, z = 0, 0, 0

for c in s:
    if c == '_':
        w = False
        x = 0
    elif c == '(':
        p = True
        w = False
        x = 0
    elif c == ')':
        p = False
        w = False
        x = 0
    else:
        x += 1
        if not p and x > y:
            y = x
        if p and not w:
            z += 1
        w = True

print(y, z)
