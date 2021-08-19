import sys
import math
n = int(input())
s = n
r = 1
while n // 10 != 0:
    n = n // 10
    r *= 10
next = (s // r + 1) * r
print(next - s)
