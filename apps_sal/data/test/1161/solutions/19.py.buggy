#!/usr/bin/env python3

import sys

s = input()
OPENING = ('<', '{', '[', '(')
CLOSING = ('>', '}', ']', ')')
result = 0
stack = []

for c in s:
    if c in OPENING:
        stack.append(c)
    else:
        if stack:
            last_br = stack.pop()
            if c != CLOSING[OPENING.index(last_br)]:
                result += 1
        else:
            print("Impossible")
            return
print("Impossible" if stack else result)
