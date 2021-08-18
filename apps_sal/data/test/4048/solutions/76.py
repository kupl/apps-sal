"""
Created on Wed Sep  9 01:55:56 2020

@author: liang
"""

import math
N = int(input())
key = int(math.sqrt(N))

ans = 10**12
for i in reversed(range(1, key + 1)):
    if N % i == 0:
        ans = i - 1 + N // i - 1
        break
print(ans)
