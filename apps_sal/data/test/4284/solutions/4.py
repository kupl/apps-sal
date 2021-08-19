# 570_C

import math

cases = int(input())

for i in range(0, cases):
    ln = [int(i) for i in input().split(" ")]
    k = ln[0]
    t = ln[1]
    a = ln[2]
    b = ln[3]
    if k / t <= b:
        print(-1)
    else:
        num = b * t
        turns = (k - num) / (a - b)
        if turns % 1 == 0:
            print(min(t, int(turns) - 1))
        else:
            print(min(t, math.floor(turns)))
