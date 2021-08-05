import sys
from itertools import *
from math import *


def solve():
    n, m, leftbank, rightbank = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    l = list(map(int, input().split()))
    smallx = leftbank
    smallxsquared = smallx * smallx
    rightbankminusleftbanksquared = (rightbank - leftbank) * (rightbank - leftbank)
    leftbest, rightbest, distbest = -1, -1, 100000000
    ll = 0
    for i, bcord, length in zip(count(), b, l):
        wanty = bcord * smallx / rightbank
        while ll < n and a[ll] <= wanty:
            ll += 1
        for pos in range(ll - 1, ll + 1):
            if pos >= 0 and pos < n:
                first = sqrt(smallxsquared + a[pos] * a[pos])
                second = sqrt(rightbankminusleftbanksquared + (bcord - a[pos]) * (bcord - a[pos]))
                totaldist = first + second + length
                if totaldist < distbest:
                    distbest = totaldist
                    leftbest = pos
                    rightbest = i
    print(leftbest + 1, rightbest + 1)


if sys.hexversion == 50594544:
    sys.stdin = open("test.txt")
solve()
