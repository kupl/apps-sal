#!/usr/bin/env python3

n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)

x = 0
y = 0
for i in range(len(a)):
    if i % 2 == 0:
        x += a[i]
    else:
        y += a[i]

print((x-y))

