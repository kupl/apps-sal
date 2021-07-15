# Author: S Mahesh Raju
# Username: maheshraju2020
# Created on: 25/09/2020 01:47:42

from sys import stdin, stdout, setrecursionlimit
import heapq
from math import gcd, ceil, sqrt
from collections import Counter, deque
from bisect import bisect_left, bisect_right
from itertools import combinations, permutations
ii1 = lambda: int(stdin.readline().strip())
is1 = lambda: stdin.readline().strip()
iia = lambda: list(map(int, stdin.readline().strip().split()))
isa = lambda: stdin.readline().strip().split()
setrecursionlimit(100000)
mod = 1000000007

def getAns(d):
    queue = [[0, 0]]
    seen = set()
    res = float("-inf")
    while len(queue):
        cur, cost = queue.pop()
        if cur not in seen:
            seen.add(cur)
            res = max(res, cost)
            for a, b in d.get(cur, []):
                queue.append([a, b + cost])
    return res


n = ii1()
d = {}
for i in range(n - 1):
    a, b, cost = iia()
    d.setdefault(a, []).append([b, cost])
    d.setdefault(b, []).append([a, cost])
print(getAns(d))

