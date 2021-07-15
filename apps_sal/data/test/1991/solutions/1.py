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

    first_wrong = -1
    first_break = -1
    skip = False

    for i, a in enumerate(A):
        if i + 1 == a:
            if first_wrong != -1 and first_break == -1:
                first_break = i
        else:
            if first_wrong == -1:
                first_wrong = i
            elif first_break != -1:
                skip = True

    if first_wrong == -1:
        print(0)
    elif not skip:
        print(1)
    else:
        print(2)






mode = 'T'

if mode == 'T':
    t = ri()
    for i in range(t):
        solve()
else:
    solve()

