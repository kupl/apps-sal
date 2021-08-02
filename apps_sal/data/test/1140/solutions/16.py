#!/usr/bin/env python3

INF = int(1e9 + 5)

n = int(input())

x, y, c1, c2 = (INF, -INF, 0, 0)

a = list(map(int, input().split()))

for i in a:
    if i > y:
        y = i
        c2 = 1
    elif i == y:
        c2 += 1
    if i < x:
        x = i
        c1 = 1
    elif i == x:
        c1 += 1
print(y - x, end=" ")
if x != y:
    print(c1 * c2)
else:
    print(c1 * (c1 - 1) // 2)
