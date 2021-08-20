from bisect import bisect_right
from sys import stdin
from functools import reduce
from math import sqrt, gcd
from itertools import permutations
from collections import defaultdict, deque, Counter
import sys
sys.setrecursionlimit(1000000)


def get_min(p):
    n = len(p)
    ret = [[] for _ in range(n)]
    for i in reversed(list(range(n))):
        if i == n - 1:
            ret[i] = [i, p[i]]
        elif p[i] < ret[i + 1][1]:
            ret[i] = [i, p[i]]
        else:
            ret[i] = ret[i + 1]
    return ret


def solve(n, p):
    p2 = get_min(p)
    left = 0
    ret = []
    while left < n - 1:
        if p[left] < p2[left + 1][1]:
            left += 1
            continue
        (right, m) = p2[left + 1]
        for i in reversed(list(range(left, right))):
            (p[i], p[i + 1]) = (p[i + 1], p[i])
            ret.append(i + 1)
        for i in range(left, right):
            if i + 1 != p[i]:
                return False
        left = right
    if len(ret) != n - 1:
        return False
    return ret


n = int(input())
p = list(map(int, input().split()))
ans = solve(n, p)
if ans:
    assert len(ans) == n - 1
if ans:
    for a in ans:
        print(a)
else:
    print(-1)
