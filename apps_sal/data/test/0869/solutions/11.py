#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

#   = input()
#   = int(input())

#() = (i for i in input().split())
#   = [i for i in input().split()]

(a, b) = (int(i) for i in input().split())
#   = [int(i) for i in input().split()]

start = time.time()

m = min(a, b)
a = divmod(a - m, 2)[0]
b = divmod(b - m, 2)[0]

print(m, a + b)
finish = time.time()
#print(finish - start)
