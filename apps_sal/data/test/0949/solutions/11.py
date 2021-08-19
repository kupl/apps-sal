#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time


(a, b) = (int(i) for i in input().split())
start = time.time()

if (a == b):
    print(a)
else:
    print(1)

finish = time.time()
#print(finish - start)
