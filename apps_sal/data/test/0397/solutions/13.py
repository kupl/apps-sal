#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time


(n, k) = (int(i) for i in input().split())


start = time.time()

print((2 * n + 3 - int((9 + 8 * (n + k))**0.5)) // 2)
finish = time.time()
#print(finish - start)
