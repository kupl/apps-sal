# -*- coding: utf-8 -*-

a, b = map(int, input().split())

mul = a * b

result = 'Even' if (mul % 2 == 0) else 'Odd'

print(result)
