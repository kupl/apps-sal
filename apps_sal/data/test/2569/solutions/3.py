from collections import defaultdict as dd
from collections import deque
import bisect
import heapq


def ri():
    return int(input())


def rl():
    return list(map(int, input().split()))


cache = [0] * (2 * 10 ** 6 + 1)
cache[3] = 4
cache[4] = 4


def solve(last):
    n = ri()
    if cache[n] != 0:
        print(cache[n])
        return last
    mod = 10 ** 9 + 7
    if n <= 2:
        print(0)
        return last
    elif n <= 4:
        print(4)
        return last
    else:
        (j, k) = last
        (a, b) = (cache[j], cache[k])
        for i in range(k + 1, n + 1):
            (a, b) = (b, (2 * a + b) % mod)
            if i % 3 == 0:
                b = (b + 4) % mod
            cache[i] = b
        last = [n - 1, n]
        print(b)
        return last


mode = 'T'
if mode == 'T':
    t = ri()
    last = [3, 4]
    for i in range(t):
        last = solve(last)
else:
    solve()
