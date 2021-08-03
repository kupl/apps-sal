from collections import defaultdict as dd
from collections import deque
import bisect
import heapq


def ri():
    return int(input())


def rl():
    return list(map(int, input().split()))


def solve():
    n, k = rl()
    A = rl()
    W = rl()
    A.sort()
    W.sort(reverse=True)

    lo, hi = 0, len(A) - 1
    answer = 0
    for w in W[::-1]:
        if w != 1:
            break
        answer += 2 * A[hi]
        hi -= 1

    for w in W:
        if w == 1:
            break
        else:
            answer += A[hi] + A[lo]
            lo += w - 1
            hi -= 1
    print(answer)


mode = 'T'

if mode == 'T':
    t = ri()
    for i in range(t):
        solve()
else:
    solve()
