#!/usr/bin/env python3

# import
#import math
#import numpy as np
N = int(input())

if N % 2 == 1:
    print((0))
else:
    ans = 0
    for i in range(50):
        ans += N // (10 * 5 ** i)

    print(ans)
