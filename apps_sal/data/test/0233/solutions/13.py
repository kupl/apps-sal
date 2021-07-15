#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

#   = input()
n     = int(input())
ans_m = 0
ans_c = 0

for i in range(n):
    (m, c) = (int(i) for i in input().split())
    if m > c:
        ans_m += 1
    elif c > m:
        ans_c += 1

start = time.time()

if ans_m>ans_c:
    print("Mishka")
elif ans_m == ans_c:
    print("Friendship is magic!^^")
else:
    print("Chris")

finish = time.time()
#print(finish - start)

