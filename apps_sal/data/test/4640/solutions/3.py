from functools import lru_cache
from itertools import accumulate
from bisect import bisect_left as bl
from bisect import bisect_right as br
from heapq import heappush, heappop, heapify
import math
from collections import *
from functools import reduce, cmp_to_key
import sys
input = sys.stdin.readline


M = mod = 998244353
def factors(n): return sorted(set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
def inv_mod(n): return pow(n, mod - 2, mod)


def li(): return [int(i) for i in input().rstrip('\n').split()]
def st(): return input().rstrip('\n')
def val(): return int(input().rstrip('\n'))
def li2(): return [i for i in input().rstrip('\n')]
def li3(): return [int(i) for i in input().rstrip('\n')]


class Node:
    def __init__(self, s, e):
        self.start = s
        self.end = e
        self.val = 0
        self.left = None
        self.right = None


def build(nums, l, r):
    if l == r:
        temp = Node(l, l)
        temp.val = nums[l]
    else:
        mid = (l + r) >> 1
        temp = Node(l, r)
        temp.left = build(nums, l, mid)
        temp.right = build(nums, mid + 1, r)
        temp.val = max(temp.left.val, temp.right.val)
    return temp


def update(root, start, value):
    if root.start == start == root.end:
        root.val = value
    elif root.start <= start and root.end >= start:
        update(root.left, start, value)
        update(root.right, start, value)
        root.val = max(root.left.val, root.right.val)


def query(root, start, end):
    if root.start >= start and root.end <= end:
        return root.val
    elif root.start > end or root.end < start:
        return -float('inf')
    else:
        temp1 = query(root.left, start, end)
        temp2 = query(root.right, start, end)
        return max(temp1, temp2)


for _ in range(val()):
    n, k = li()
    l = li()
    y = li()

    l.sort()

    dp = [0] * (n + 1)

    for i in range(n - 1, -1, -1):
        curright = br(l, l[i] + k)
        totnow = curright - i
        dp[i] = totnow

    # print(l, k)
    # print(dp)

    root = build(dp, 0, n)

    for i in range(n):
        curright = br(l, l[i] + k)
        dp[i] += query(root, curright, n)
    print(max(dp))
