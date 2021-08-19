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
    word = 'codeforces'
    mult = [1] * 10
    count = 1
    i = -1
    while count < n:
        i = (i + 1) % 10
        mult[i] += 1
        count = count // (mult[i] - 1) * mult[i]
    out = ''
    for i in range(10):
        out += word[i] * mult[i]
    print(out)


mode = 's'
if mode == 'T':
    t = ri()
    for i in range(t):
        solve()
else:
    solve()
