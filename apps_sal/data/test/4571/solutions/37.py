#!/usr/bin/env python3

# import
#import math
#import numpy as np
# = int(input())
# = input()
N, M = list(map(int, input().split()))

print(((1900 * M + 100 * (N - M)) * 2 ** M))
