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
    answer = 0
    half = (n + 1) // 2
    for i in range(1, half):
        ring = (2 * i + 1)**2 - (2 * i - 1)**2
        answer += i * ring
    print(answer)


mode = 'T'

if mode == 'T':
    t = ri()
    for i in range(t):
        solve()
else:
    solve()
