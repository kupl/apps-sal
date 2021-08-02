#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n, m = list(map(int, input().split(' ')))
distances = [0] * 1000

for l in [input() for _ in range(n)]:
    distance = l.index('S') - l.index('G')
    if distance < 0:
        print(-1)
        return
    distances[distance] = 1

print(distances.count(1))
