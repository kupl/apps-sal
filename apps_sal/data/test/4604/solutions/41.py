import sys
import heapq
import math
from itertools import zip_longest, permutations, combinations, combinations_with_replacement
from itertools import accumulate, dropwhile, takewhile, groupby
from functools import lru_cache
from copy import deepcopy
N = int(input())
A = list(map(int, input().split()))
B = [0] * N
for a in A:
    B[a] += 1
ok = True
if N % 2 == 1:
    ok = ok and B[0] == 1
    for i in range(1, N):
        ok = ok and B[i] == (2 if i % 2 == 0 else 0)
else:
    for i in range(N):
        ok = ok and B[i] == (0 if i % 2 == 0 else 2)
ans = 1
MOD = int(1000000000.0) + 7
for _ in range(N // 2):
    ans *= 2
    ans %= MOD
print(ans if ok else 0)
