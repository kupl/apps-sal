#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

n       = int(input())
bus     = []
flag    = True

for i in range(n):
    x = list(input())
    if flag:
        if x[0] == 'O' and x[1] == 'O':
            x[0] = '+'
            x[1] = '+'
            flag = False
        elif x[3] == 'O' and x[4] == 'O':
            x[3] = '+'
            x[4] = '+'
            flag = False
    bus.append(x)
start = time.time()

if flag:
    print('NO')
else:
    print('YES')
    for i in range(n):
        for j in bus[i]:
            print(j, end='')
        print()
finish = time.time()
#print(finish - start)

