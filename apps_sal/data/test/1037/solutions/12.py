from collections import *
from itertools import *

N = int(input())

A = list(map(int, input().split()))
SA = SB = 0
ABI = sorted(((b := max(N - i, i - 1) * a, SA := SA + a, SB := SB + b) and (a, b, i) for i, a in enumerate(A, 1)), reverse=True)

prev = {0: 0}
prev_max = 0
for k, (a, b, i) in enumerate(ABI):
    curr = defaultdict(int)
    curr_max = 0
    for l, p in list(prev.items()):
        r = k - l
        if p + SB - min(l, r) * SA < prev_max:
            continue
        curr[l] = max(curr[l], p + abs(N - i - r) * a)
        curr[l + 1] = p + abs(i - l - 1) * a
        curr_max = max(curr_max, curr[l], curr[l + 1])
    SA -= a
    SB -= b
    prev = curr
    prev_max = curr_max

print(curr_max)
