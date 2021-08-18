from decimal import Decimal
from copy import deepcopy
import heapq
from heapq import heappush
from heapq import heappop
from heapq import heapify
import itertools
from bisect import insort_left
from bisect import bisect_right
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
H, W, D = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(H)]
table = [[-1, -1] for _ in range(H * W + 1)]
for i in range(H):
    for j in range(W):
        a = A[i][j]
        if a > D:
            table[a - D][0] = i
            table[a - D][1] = j
magic = [0] * (H * W + 1)
for i in range(H):
    for j in range(W):
        a = A[i][j]
        if a <= H * W - D:
            magic[a] = abs(i - table[a][0]) + abs(j - table[a][1])
for i in range(D + 1, H * W + 1):
    magic[i] += magic[i - D]
Q = int(input())
ans = 0
for i in range(Q):
    L, R = list(map(int, input().split()))
    if L == R:
        print((0))
    else:
        if L <= D:
            print((magic[R - D]))
        else:
            print((magic[R - D] - magic[L - D]))
