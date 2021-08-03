#!/usr/bin/env python
# -.- coding: utf-8 -.-

k, n, w = (int(item) for item in input().strip().split(" "))
acc = 0
i = 1
totals = (k * w + 1 * k) * w // 2
print((0, totals - n)[(totals - n) > 0])
