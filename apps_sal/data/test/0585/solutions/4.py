from collections import defaultdict as dd
from collections import deque
import bisect
import heapq


def ri():
    return int(input())


def rl():
    return list(map(int, input().split()))


def solve():
    (n, m) = rl()
    A = rl()
    B = rl()
    mod = 998244353
    if A[0] < B[0]:
        print(0)
        return
    mins = dd(int)
    _min = A[-1]
    for a in A[::-1]:
        _min = min(_min, a)
        mins[_min] += 1
    if _min != B[0]:
        print(0)
        return
    answer = 1
    for b in B[1:]:
        if mins[b] == 0:
            print(0)
            return
        else:
            answer = answer * mins[b] % mod
    print(answer)


mode = 'S'
if mode == 'T':
    t = ri()
    for i in range(t):
        solve()
else:
    solve()
