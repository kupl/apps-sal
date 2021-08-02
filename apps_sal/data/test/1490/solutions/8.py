#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

(n, m) = (int(i) for i in input().split())
a = sorted([int(i) for i in input().split()])

start = time.time()


acc = 0
ans = []

j = 0
sum = 0

for i in range(1, 1000000001):
    if j < n:
        if i == a[j]:
            j += 1
            continue

    if sum + i > m:
        break

    sum += i
    acc += 1
    ans.append(i)

print(acc)
for i in range(acc):
    print(ans[i], end=' ')
print()

#finish = time.time()
#print(finish - start)
