import math
from math import *
n, b, p = map(int, input().split(' '))
ansb = 0
ansp = p * n
while n > 1:
    t = floor(log(n) / log(2))
    m = 2**t
    ansb += (2 * b + 1) * (m / 2)
    n -= m / 2
print(int(ansb), int(ansp))
