import sys
import heapq, math
from itertools import zip_longest, permutations, combinations, combinations_with_replacement
from itertools import accumulate, dropwhile, takewhile, groupby
from functools import lru_cache
from copy import deepcopy

N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

B = {}
s = 0
ans = 0
B[0] = 1
for a in A:
    s = (s + a) % M
    ans += B.get(s, 0)
    B[s] = B.get(s, 0) + 1

print(ans)

