from math import *
from random import *
for t in range(int(input())):
    (a, b, n) = map(int, input().split())
    otv = 0
    while a <= n and b <= n:
        if a > b:
            b += a
        else:
            a += b
        otv += 1
    print(otv)
