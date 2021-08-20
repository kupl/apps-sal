import sys
import math
from collections import defaultdict


def input():
    return sys.stdin.readline().rstrip()


for t in range(int(input())):
    (s, i, e) = map(int, input().split())
    x = (i + e - s) / 2
    if x < 0:
        print(e + 1)
    elif x == 0:
        print(e)
    elif x >= e:
        print(0)
    else:
        print(e - int(x))
