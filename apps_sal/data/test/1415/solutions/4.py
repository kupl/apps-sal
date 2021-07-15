#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

#   = input()
#   = int(input())

#() = (i for i in input().split())
#   = [i for i in input().split()]

(a, b, x, y) = (int(i) for i in input().split())

s   = input()
ans = [0 for i in range(len(s) + 1) ]

start = time.time()

acc = 0
x  -= 1
y  -= 1

map = [[ 0 for i in range(b)] for j in range(a)]

for i in range(len(s)):
    if map[x][y] == 0:
        ans[i] += 1
        map[x][y] = 1
    if s[i] == 'L' and y > 0:
        y -= 1
    elif s[i] == 'R' and y < b-1:
        y += 1
    elif s[i] == 'D' and x < a-1:
        x += 1
    elif s[i] == 'U' and x > 0:
        x -= 1


ans[len(s)] = a*b - sum([sum(i) for i in map])

for i in ans:
    print(i, end= ' ')
print()
finish = time.time()
#print(finish - start)

