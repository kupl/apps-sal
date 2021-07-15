#!/usr/bin/env python3

(n, m) = tuple(map(int, input().split()))

x = []
for i in range(m):
    pair = tuple(map(int, input().split()))
    x.append(pair)

if m == 1:
    print('YES')
    return

s = None
top = x[0][0]
for i in range(1, m):
    if x[i][0] != top and x[i][1] != top:
        if s is None:
            s = set(x[i])
        else:
            s &= set(x[i])
if s is None or len(s) != 0:
    print('YES')
    return

s = None
top = x[0][1]
for i in range(1, m):
    if x[i][0] != top and x[i][1] != top:
        if s is None:
            s = set(x[i])
        else:
            s &= set(x[i])
if s is None or len(s) != 0:
    print('YES')
    return

print('NO')

