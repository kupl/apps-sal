#!/usr/bin/env python3

#import
#import math
#import numpy as np
K = int(input())
A, B = list(map(int, input().split()))

for i in range(1000):
    if A <= K * i <= B:
        print("OK")
        return

print("NG")

