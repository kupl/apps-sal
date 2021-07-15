#!/usr/bin/env python3

#import
#import math
#import numpy as np
A, B, C, K = list(map(int, input().split()))

print((min(A, K) - max(0, K - (A + B))))



