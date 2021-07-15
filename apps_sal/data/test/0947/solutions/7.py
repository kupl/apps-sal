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
    if n % 2 == 0:
        print(n // 2, n // 2)
    else:
        sq = int(n**0.5) + 2
        for i in range(3, sq):
            if n % i == 0:
                print(n // i, n - n // i)
                return
        print(1, n - 1)
        return






mode = 'T'

if mode == 'T':
    t = ri()
    for i in range(t):
        solve()
else:
    solve()

