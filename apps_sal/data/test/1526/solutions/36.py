import copy
import sys
import math

tmp = input().split()
a, b, c = list([int(a) for a in tmp])

hoge = max(a, b, c) * 3 - a - b - c
if(hoge % 2 == 0):
    print((hoge // 2))
else:
    print((hoge // 2 + 2))
