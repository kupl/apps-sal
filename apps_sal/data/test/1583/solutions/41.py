import sys
from math import *

input = sys.stdin.readline

a, b, x = list(map(int, input().split()))

s = x / a


if s > a*b / 2:
    sankaku = a*b - s
    h = (a*b - s) * 2 / a 
    print((degrees(atan(h/a))))
else:
    w = 2*s/b
    print((degrees(atan(b/w))))

