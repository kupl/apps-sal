#!/usr/bin/env python3

# import
import math
#import numpy as np
# = int(input())
# = input()
a, b, x = list(map(int, input().split()))
# = list(map(int, input().split()))
# = [input(), input()]
# = [list(map(int, input().split())) for _ in range(N)]
# = [int(input()) for _ in range(N)]
# = {i:[] for i in range(N)}

d = a * a * b

# 半分より多い
if x * 2 > d:
    x = d - x
    xx = 2 * x / (a * a * a)
    theta = math.atan(xx)
    print((theta * 180 / math.pi))

else:
    xx = 2 * x / (a * b * b)
    theta = math.atan(xx)
    print((90 - theta * 180 / math.pi))
