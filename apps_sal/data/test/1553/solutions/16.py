#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n, h = map(int, input().split())
arr = list(map(int, input().split()))

use = []
for i in range(n):
    use.append(arr[i])
    use.sort()
    real_use = use[-1:-(i + 2):-2]
    # print(real_use)
    if sum(real_use) > h:
        print(i)
        return
print(n)
