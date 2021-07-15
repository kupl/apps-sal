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
    k = 7 + 3 * (n - 1)
    print (k)
    print(0, 0)
    print(0, 1)
    for i in range(1, n + 1):
        print(i, i - 1)
        print(i, i)
        print(i, i + 1)
    print(n + 1, n)
    print(n + 1, n + 1)






mode = 's'

if mode == 'T':
    t = ri()
    for i in range(t):
        solve()
else:
    solve()

