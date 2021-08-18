from bisect import bisect_left as bl
from bisect import bisect_right as br
import heapq
import math
from collections import *
from functools import reduce, cmp_to_key
import sys
input = sys.stdin.readline


def li(): return [int(i) for i in input().rstrip('\n').split()]
def st(): return input().rstrip('\n')
def val(): return int(input().rstrip('\n'))
def li2(): return [i for i in input().rstrip('\n').split(' ')]
def li3(): return [int(i) for i in input().rstrip('\n')]


def givediff(a, b):
    return sum(max(i, j) for i, j in zip(b, a))


n, m, k = li()
l = []
for i in range(n):
    l.append(li())


l1 = [deque() for i in range(m)]
for i in range(m):
    l1[i].append([0, l[0][i]])


i, j = 0, 1
ans = 0
perm = [0] * m if sum(l[0]) > k else l[0][:]

curr = l[0][:]
while j != n:

    for itr in range(m):
        while len(l1[itr]) and l1[itr][-1][-1] <= l[j][itr]:
            l1[itr].pop()
        l1[itr].append([j, l[j][itr]])

    while i < j and givediff(curr, l[j]) > k:
        i += 1

        for itr in range(m):
            while l1[itr][0][0] < i:
                l1[itr].popleft()
            curr[itr] = l1[itr][0][-1]

    for itr in range(m):
        curr[itr] = l1[itr][0][-1]

    if ans < j - i + 1 and givediff(l[j], curr) <= k:
        ans = j - i + 1
        perm = [max(a, b) for a, b in zip(l[j], curr)]

    j += 1
print(*perm)
