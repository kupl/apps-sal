from collections import *
from heapq import *
from math import *


t = int(input())
while t:
    t -= 1
    flag = False
    n, m = [int(x) for x in input().split()]
    for i in range(n):
        a, b = [int(x) for x in input().split()]
        c, d = [int(x) for x in input().split()]
        if b == c:
            flag = True
    if m % 2:
        print("NO")
    elif flag:
        print("YES")
    else:
        print("NO")
