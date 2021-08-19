import sys
from collections import Counter
from math import *
for _ in range(int(input())):
    (a, b, c) = map(int, input().split())
    if a > b + c + 1 or b > a + c + 1 or c > a + b + 1:
        print('No')
    else:
        print('Yes')
