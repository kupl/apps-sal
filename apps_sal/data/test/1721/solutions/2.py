from functools import lru_cache
from itertools import accumulate, permutations
from bisect import bisect_left as bl
from bisect import bisect_right as br
from heapq import heappush, heappop, heapify
import math
from collections import *
from functools import reduce, cmp_to_key
import sys
input = sys.stdin.readline
M = mod = 998244353


def factors(n):
    return sorted(set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0))))


def inv_mod(n):
    return pow(n, mod - 2, mod)


def li():
    return [int(i) for i in input().rstrip('\n').split()]


def st():
    return input().rstrip('\n')


def val():
    return int(input().rstrip('\n'))


def li2():
    return [i for i in input().rstrip('\n')]


def li3():
    return [int(i) for i in input().rstrip('\n')]


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
        mid = l + r >> 1
        temp = Node(l, r)
        temp.left = build(nums, l, mid)
        temp.right = build(nums, mid + 1, r)
        temp.val = temp.left.val + temp.right.val
    return temp


def update(root, start, value):
    if root.start == start == root.end:
        root.val += value
    elif root.start <= start and root.end >= start:
        update(root.left, start, value)
        update(root.right, start, value)
        root.val = root.left.val + root.right.val


def query(root, start, end):
    if root.start >= start and root.end <= end:
        return root.val
    elif root.start > end or root.end < start:
        return 0
    else:
        temp1 = query(root.left, start, end)
        temp2 = query(root.right, start, end)
        return temp1 + temp2


n = val()
s = st()
index = defaultdict(deque)
for i in range(n):
    index[s[i]].append(i)
s1 = s[::-1]
N = 2 * 10 ** 5 + 10
root = build([0] * N, 0, N - 1)
ans = 0
pointer = 0
myset = set()
for i in range(n):
    ind1 = index[s1[i]].popleft()
    if ind1 == pointer:
        myset.add(pointer)
        while pointer in myset:
            pointer += 1
    else:
        myset.add(ind1)
        ans += ind1 - pointer
        ans -= query(root, pointer, ind1)
    update(root, ind1, 1)
print(ans)
