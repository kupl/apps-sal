import sys
from heapq import heappush, heappop, heapify
import math
from math import gcd
import itertools as it
from collections import deque

input = sys.stdin.readline


def inp():
    return int(input())


def inpl():
    return list(map(int, input().split()))


INF = 1001001001


def main():
    n = inp()
    k = inp()
    x = inp()
    y = inp()
    if n > k:
        print((x * k + y * (n - k)))
    else:
        print((x * n))


main()
