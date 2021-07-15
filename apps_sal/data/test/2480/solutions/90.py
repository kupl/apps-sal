import sys
from collections import defaultdict
from collections import deque
import numpy as np
import heapq
from heapq import heappush, heappop
import itertools


# read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 7)

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

A = [0] + A
A = list(itertools.accumulate(A))
A = [x % K for x in A]

cnt = defaultdict(int)
ans = 0
for i, a in enumerate(A):
    x = (a - i) % K
    #print("i", i, "a", a, "x", x, "cnt", cnt)

    ans += cnt[x]
    cnt[x] += 1

    if i >= K-1:
        y = (A[i-K+1] - (i-K+1)) % K
        cnt[y] -= 1

print(ans)

