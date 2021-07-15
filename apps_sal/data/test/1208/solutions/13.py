#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n       = int(input())
now     = 0
max     = 0
readers = []

for i in range(n):
    (flag, N)  = (i for i in input().split())
    if flag == '+':
        now += 1
        if now > max:
            max = now

    else:
        if N not in readers:
            max += 1
        else:
            now -= 1

    if N not in readers:
        readers.append(N)

print(max)


