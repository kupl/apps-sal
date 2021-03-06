import numpy as np
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
sys.setrecursionlimit(10 ** 7)
INF = float('inf')
(M, K) = map(int, input().split())
if M == 1:
    if K == 0:
        ans = [0, 0, 1, 1]
        print(*ans)
    else:
        print(-1)
elif K > 2 ** M - 1:
    print(-1)
elif K == 0:
    ans = []
    for i in range(2 ** M):
        ans.append(i)
        ans.append(i)
    print(*ans)
else:
    ans = deque([K])
    for i in range(2 ** M):
        if i == K:
            continue
        ans.append(i)
        ans.appendleft(i)
    ans.append(K)
    print(*ans)
