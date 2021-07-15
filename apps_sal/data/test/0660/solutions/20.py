#!/usr/bin/env python
n, b, p = list(map(int, input().split()))
b_sum = 0
p_sum = p * n
import math
while n > 1:
    b_sum += (2 * b + 1) * int(math.log2(n))
    n -= int(math.log2(n))
print(b_sum, p_sum)

