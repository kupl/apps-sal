#!/usr/bin/env python
# -.- coding: utf-8 -.-

n = int(input())
cool_factors = [int(item) for item in input().strip().split(" ")]
cool_factors.sort()
acc = 0
for i in range(1, len(cool_factors)):
    if cool_factors[i] <= cool_factors[i - 1]:
        diff = cool_factors[i - 1] - cool_factors[i] + 1
        cool_factors[i] = cool_factors[i - 1] + 1
        acc += diff
print(acc)
