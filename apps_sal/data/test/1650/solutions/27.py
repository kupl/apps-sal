import sys
import itertools
import time
import math
from heapq import heappop, heappush
from collections import defaultdict
from collections import Counter
from collections import deque
from itertools import permutations
sys.setrecursionlimit(10 ** 7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
L = input()
dp = [[0] * 2 for _ in range(len(L) + 1)]
dp[0][0] = 2
dp[0][1] = 1
for i in range(1, len(L)):
    if L[i] == '1':
        dp[i][0] = 2 * dp[i - 1][0] % MOD
        dp[i][1] = (dp[i - 1][1] * 3 + dp[i - 1][0]) % MOD
    else:
        dp[i][0] = dp[i - 1][0]
        dp[i][1] = 3 * dp[i - 1][1] % MOD
print(sum(dp[len(L) - 1]) % MOD)
