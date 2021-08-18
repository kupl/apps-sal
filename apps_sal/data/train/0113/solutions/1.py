import sys
import math

for _ in range(int(input())):
    a, b = map(int, input().split())
    x = abs(a - b)
    res = x // 5
    x %= 5
    res += x // 2
    x %= 2
    print(res + x)
