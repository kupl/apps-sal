import numpy as np
from copy import deepcopy
import heapq
from heapq import heappush
from heapq import heappop
from heapq import heapify
import itertools
from bisect import insort_left
from bisect import bisect_left
from collections import deque
import math
import fractions
from collections import Counter
from collections import defaultdict
from itertools import combinations
from itertools import permutations
from itertools import accumulate
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
alf = list("abcdefghijklmnopqrstuvwxyz")
ALF = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
INF = float("inf")
N, S = list(map(int, input().split()))
MOD = 998244353
A = list(map(int, input().split()))
dp = np.zeros(S + 1, dtype=np.int64)
dp[0] = 2
if A[0] <= S:
    dp[A[0]] = 1
for i in range(1, N):
    a = A[i]
    p = dp * 2
    if a <= S:
        p[a:] += dp[:-a]
    p %= MOD
    dp = p
print((dp[-1]))
