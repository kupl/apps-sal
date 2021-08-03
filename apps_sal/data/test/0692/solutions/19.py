#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time


def lcm(a, b):
    return(a * b // gcd(a, b))


def gcd(a, b):
    while(b != 0):
        while(a >= b):
            a -= b
        (a, b) = (b, a)
    return(a)


n = int(input())

M = [int(i) for i in input().split()]
R = [int(i) for i in input().split()]

start = time.time()

m = 1

for i in range(n):
    m = lcm(m, M[i])

a = [0 for i in range(m)]

for i in range(n):
    if R[i] >= M[i]:
        continue

    now = R[i] - 1
    if now < 0:
        now += M[i]

    while (now < m):
        a[now] = 1
        now += M[i]

print(sum(a) / m)
finish = time.time()
#print(finish - start)
