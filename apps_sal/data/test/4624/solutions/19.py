from collections import *
from heapq import *
from math import *


t = int(input())
while t:
    t -= 1
    n, x = [int(x) for x in input().split()]
    if n <= 2:
        print(1)
    else:
        n -= 2
        print(1 + ceil(n / x))
