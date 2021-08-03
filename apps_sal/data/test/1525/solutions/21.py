#import sys
#import numpy as np
import math
#from fractions import Fraction
import itertools
from collections import deque
from collections import Counter
#import heapq
#from fractions  import gcd
# input=sys.stdin.readline
#import bisect
Mod = 10**9 + 7
h, w, K = list(map(int, input().split()))
dp = [[0] * w for _ in range(h + 1)]
dp[0][0] = 1
n = 2**(w - 1)
for i in range(h):
    for j in range(w):
        for m in range(n):
            ok = True
            for k in range(w - 2):
                if (m & (1 << k)) and (m & (1 << (k + 1))):
                    ok = False
            if not ok:
                continue
            nj = j
            if (m & (1 << j)):
                nj = j + 1
            elif j > 0 and (m & (1 << (j - 1))):
                nj = j - 1
            dp[i + 1][nj] += dp[i][j]
            dp[i + 1][nj] %= Mod
print((dp[h][K - 1]))
