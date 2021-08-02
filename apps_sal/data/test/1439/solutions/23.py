
# -*- coding: utf-8 -*-

n, m = list(map(int, input().split()))
p = [0] * m
for x in map(int, input().split()):
    n = p[:]
    n[x % m] = 1
    for i in range(m):
        if p[i] == 1:
            n[(i + x) % m] = 1
    p = n
    if p[0]:
        print('YES')
        return

print('NO')
