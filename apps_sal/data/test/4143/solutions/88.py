#!/usr/bin/env python3

# import
import math
#import numpy as np
N = int(input())
A = [int(input()) for _ in range(5)]

a = min(A)

print((math.ceil(N / a) + 4))
