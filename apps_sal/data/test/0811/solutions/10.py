# -*- coding: utf-8 -*-

a, b = list(map(int, input().split()))

n = 0
shorele = 0

while a > 0:
    n += a
    shorele += a
    a = shorele // b
    shorele = shorele % b


print(n)
