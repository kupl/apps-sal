from collections import Counter

import sys
from itertools import accumulate


def go():
    n, k = list(map(int, input().split()))
    a = sorted(map(int, input().split()))
    c = Counter(a)
    if max(c.values()) >= k:
        return 0

    upsum = {}
    upcnt = {}
    prev = -1
    cursum = 0
    for cnt, aa in enumerate(a):
        if aa != prev:
            upsum[aa] = cursum
            upcnt[aa] = cnt
        cursum += aa
        prev = aa

    downsum = {}
    downcnt = {}
    prev = -1
    cursum = 0
    for cnt, aa in enumerate(reversed(a)):
        if aa != prev:
            downsum[aa] = cursum
            downcnt[aa] = cnt
        cursum += aa
        prev = aa

    best = cursum
    for target, cnt in list(c.items()):
        need = k - cnt
        if upcnt[target] >= need:
            best = min(best, (target - 1) * upcnt[target] - upsum[target] + need)
        if downcnt[target] >= need:
            best = min(best, downsum[target] - (target + 1) * downcnt[target] + need)
        best = min(best, (target - 1) * upcnt[target] - upsum[target] +
                   downsum[target] - (target + 1) * downcnt[target] + need
                   )

    return best


t = 1
for _ in range(t):
    print(go())
