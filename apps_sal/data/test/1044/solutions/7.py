#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time


n       = int(input())
a       = [int(i) for i in input().split()]
steps   = 0
ans     = []
start = time.time()

for now in a:
    steps += now-1
    if steps%2 == 0:
        ans.append(2)
    else:
        ans.append(1)

for now in ans:
    print(now)
finish = time.time()
#print(finish - start)

