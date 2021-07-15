#!/usr/bin/env python3

#import
#import math
#import numpy as np
A, B, N = map(int, input().split())

x = min(B - 1, N)
print(int(A * x / B) - A * int(x / B))
