from collections import defaultdict as dd
from collections import deque
import bisect
import heapq


def ri():
    return int(input())


def rl():
    return list(map(int, input().split()))


def solve():
    (a, b, n) = rl()
    steps = 0
    while max(a, b) <= n:
        steps += 1
        if a <= b:
            a = a + b
        else:
            b = a + b
    print(steps)


mode = 'T'
if mode == 'T':
    t = ri()
    for i in range(t):
        solve()
else:
    solve()
