#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time


def test(a, b, C, s, n, l, r, x, p):
    if C == []:
        if s >= l and s <= r and b - a >= x:
            #            print("!!!!!!!!", a, b, C, s, p)
            return 1
        return 0

    if s >= l and s <= r and b - a >= x:
        acc = 1
    else:
        acc = 0

#    print(a, b, C, s, p)
    for i in range(len(C)):

        if s + C[i] <= r:
            acc += test(min(a, C[i]), max(b, C[i]), C[i + 1:], s + C[i], n, l, r, x, p + [C[i]])

    return acc


(n, l, r, x) = (int(i) for i in input().split())
C = sorted([int(i) for i in input().split()])
# print(C)

start = time.time()
acc = 0

for i in range(len(C)):
    acc += test(C[i], C[i], C[i + 1:], C[i], n, l, r, x, [C[i]])

print(acc)
finish = time.time()
#print(finish - start)
