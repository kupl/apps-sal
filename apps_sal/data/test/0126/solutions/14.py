#! /usr/bin/env python3

import sys

n = int(input())
s = list(map(lambda x: int(x) - int('0'), input()))

d = [(1, 3)] + [(i, j) for j in range(3) for i in range(3)]

for u in range(10):
    if u == s[0]:
        continue
    x, y = d[u]
    for i in range(1, n):
        dx, dy = (d[s[i]][0] - d[s[i - 1]][0], d[s[i]][1] - d[s[i - 1]][1])
        x += dx
        y += dy
        if (x, y) not in d:
            break
    else:
        print(u, file=sys.stderr)
        print('NO')
        return

print('YES')

