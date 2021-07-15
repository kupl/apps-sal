#!/usr/bin/env python3

#import
import math
#import numpy as np
A, B, H, M = list(map(int, input().split()))

h = H * 30 + M / 2
m = M * 6
t = max(m, h) - min(m, h)
theta = min(t, 360 - t)
c = A**2 + B**2 - 2 * A * B * math.cos(theta / 180 * math.pi)
print((math.sqrt(c)))

