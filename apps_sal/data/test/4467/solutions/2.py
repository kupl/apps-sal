import sys
import heapq
import math
from itertools import zip_longest, permutations, combinations, combinations_with_replacement
from itertools import accumulate, dropwhile, takewhile, groupby
from functools import lru_cache
from copy import deepcopy

sys.setrecursionlimit(10000000)

N = int(input())
AB = []
CD = []

for i in range(N):
    A, B = map(int, input().split())
    AB.append((A, B))

for i in range(N):
    C, D = map(int, input().split())
    CD.append((C, D))

AB.sort()
CD.sort()

used = [False] * N
cnt = 0

for i in range(N):
    m = -1
    for j in range(N):
        if not used[j] and CD[i][0] > AB[j][0] and CD[i][1] > AB[j][1]:
            if m < 0 or AB[m][1] < AB[j][1]:
                m = j

    if m >= 0:
        used[m] = True
        cnt += 1

print(cnt)
