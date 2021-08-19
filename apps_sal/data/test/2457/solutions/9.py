from math import *
from random import *
for t in range(int(input())):
    (n, a, b, c, d) = map(int, input().split())
    if n * (a + b) < c - d or n * (a - b) > c + d:
        print('No')
    else:
        print('Yes')
