"""Codeforces Round #552 (Div. 3)

Problem F. Shovels Shop

:author:         Kitchen Tong
:mail:    kctong529@gmail.com

Please feel free to contact me if you have any question
regarding the implementation below.
"""
__version__ = '2.0'
__date__ = '2019-04-17'
import sys
from heapq import heappush, heappop


def buy_shovels(k, shovels, discounts):
    if 1 not in discounts:
        discounts[1] = 0
    accums = [0]
    for s in shovels:
        accums.append(s + accums[-1])
    for i in range(k):
        for (x, y) in list(discounts.items()):
            if i + x > k:
                continue
            perhaps = accums[i] + sum(shovels[i + y:i + x])
            accums[i + x] = min(accums[i + x], perhaps)
    return accums[-1]


def main(argv=None):
    (n, m, k) = list(map(int, input().split()))
    costs = list(map(int, input().split()))
    discounts = dict()
    for line in range(m):
        (x, y) = list(map(int, input().split()))
        if x > k:
            continue
        if x not in discounts:
            discounts[x] = y
        else:
            discounts[x] = max(discounts[x], y)
    print(buy_shovels(k, sorted(costs)[:k], discounts))
    return 0


def __starting_point():
    STATUS = main()
    return STATUS


__starting_point()
