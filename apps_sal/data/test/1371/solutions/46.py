#!/usr/bin/env python3

# import
#import math
#import numpy as np
S = int(input())


def mod(num):
    return num % (10 ** 9 + 7)


dp = [0] * (S + 10)

dp[0] = 1

if S < 3:
    print(0)
    return

for i in range(3, S + 10):
    dp[i] = mod(dp[i - 1] + dp[i - 3])

print(dp[S])
