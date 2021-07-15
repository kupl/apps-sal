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
    s = input()
    blocks = [len(b) for b in s.split('1')]
    if len(blocks) == 1:
        print((blocks[0] + k) // (k + 1))
        return
    else:
        total = blocks[0] // (k + 1) + blocks[-1] // (k + 1)
        for b in blocks[1:-1]:
            total += max(0, (b - k) // (k + 1))

    print (total)
    # print (blocks)





mode = 'T'

if mode == 'T':
    t = ri()
    for i in range(t):
        solve()
else:
    solve()

