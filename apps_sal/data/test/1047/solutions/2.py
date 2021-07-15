#!/usr/bin/env python3

n = list(map(int, input()))

elems = []
while sum(n) > 0:
    x = ''
    for i, v in enumerate(n):
        if v:
            x += '1'
            n[i] -= 1
        else:
            x += '0'
    elems.append(int(x))

print(len(elems))
print(*elems)

