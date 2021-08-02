#!/usr/bin/env python3
# -*- coding: utf-8 -*-

(n, k, p, x, y) = (int(i) for i in input().split())
a = [int(i) for i in input().split()]

a_l = 0
a_g = 0

for i in a:
    if i < y:
        a_l += 1
    else:
        a_g += 1


if a_l > (n - 1) / 2:
    print(-1)
elif a_g > (n - 1) / 2:
    sum_a = sum(a) + n - k
    if (sum_a <= x):
        for i in range(n - k):
            print(1, end=' ')
        print()
    else:
        print(-1)
else:
    sum_a = sum(a) + int((n + 1) / 2 - a_g) * y + (n - 1) / 2 - a_l
    if (sum_a <= x):
        for i in range(int((n - 1) / 2) - a_l):
            print(1, end=' ')
        for i in range(int((n + 1) / 2) - a_g):
            print(y, end=' ')
        print()
    else:
        print(-1)
