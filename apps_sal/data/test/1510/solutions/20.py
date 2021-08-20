import os
import sys
import bisect
import copy
from collections import defaultdict, Counter, deque
from functools import lru_cache
if os.path.exists('in.txt'):
    sys.stdin = open('in.txt', 'r')
if os.path.exists('out.txt'):
    sys.stdout = open('out.txt', 'w')


def input():
    return sys.stdin.readline()


def mapi(arg=0):
    return map(int if arg == 0 else str, input().split())


(n, m) = mapi()
a = list(mapi())
b = list(mapi())
res = 10 ** 18
l = 1
r = 10 ** 9
cnt = 0


def check(k):
    ans = 0
    for i in a:
        if i < k:
            ans += k - i
    for i in b:
        if i > k:
            ans += i - k
    return ans


while r - l >= 0 and cnt <= 64:
    cnt += 1
    mid1 = l + (r - l) // 3
    mid2 = r - (r - l) // 3
    if mid1 - l < 0 or r - mid1 < 0 or mid2 - l < 0 or (r - mid2 < 0):
        break
    ans1 = check(mid1)
    ans2 = check(mid2)
    res = min(res, ans1, ans2)
    if ans1 < ans2:
        r = mid2
    else:
        l = mid1
print(res)
