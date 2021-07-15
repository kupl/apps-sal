from collections import defaultdict as dd
from collections import deque
import bisect
import heapq

def ri():
    return int(input())

def rl():
    return list(map(int, input().split()))


def solve():
    n = ri()
    A = rl()
    odd_total = 0
    even_total = 0
    for i in range(n):
        if i % 2 == 0:
            even_total += A[i]
        else:
            odd_total += A[i]

    best = 0
    even_before = 0
    odd_before = 0
    even_after = even_total
    odd_after = odd_total
    for i in range(n):
        if i % 2 == 0:
            even_after -= A[i]
            even_before += A[i]
            candidate = even_before + odd_after
        else:
            odd_after -= A[i]
            odd_before += A[i]
            candidate = odd_before + even_after
        best = max(best, candidate)

    print (best)





mode = 's'

if mode == 'T':
    t = ri()
    for i in range(t):
        solve()
else:
    solve()

