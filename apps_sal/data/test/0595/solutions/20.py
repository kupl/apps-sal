#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

def func(y):
    if (y % 400 == 0 ) or ((y % 4 == 0) and (y%100 != 0)) :
        return 2
    return 1

y   = int(input())

start = time.time()

sum = 0
now = func(y)
f   = 0

while ((sum %7 != 0) or (now != f)):
    y = y + 1
    f = func(y)
    sum = sum + f

print(y)
finish = time.time()
#print(finish - start)

