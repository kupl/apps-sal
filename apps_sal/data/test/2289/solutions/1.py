import sys
import math
import bisect
import itertools
(n, q) = list(map(int, sys.stdin.readline().strip().split(' ')))
a = list(map(int, sys.stdin.readline().strip().split(' ')))
prefix_sum = list(itertools.accumulate(a))
k = list(map(int, sys.stdin.readline().strip().split(' ')))
k_sum = 0
for q0 in range(q):
    k_sum += k[q0]
    idx = bisect.bisect_left(prefix_sum, k_sum)
    if idx < n and prefix_sum[idx] == k_sum:
        idx += 1
    if idx == n:
        print(n)
        k_sum = 0
    else:
        print(n - idx)
