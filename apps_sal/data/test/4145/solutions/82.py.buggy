#!/usr/bin/env python3
import math
x = int(input())
while True:
    key = 1
    for k in range(2, int(math.sqrt(x)) + 1):
        if x % k == 0:
            key = 0
    if key == 1:
        print(x)
        return
    else:
        x += 1
print(x)
