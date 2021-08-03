#!/usr/bin/env python3
import math
a, b, c = list(map(int, input().split()))
if (b > a and c <= 0) or (b < a and c >= 0):
    print('NO')
elif b == a:
    print('YES')
else:
    print('YES' if abs(b - a) % abs(c) == 0 else 'NO')
