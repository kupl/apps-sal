from sys import stdin, stdout
from collections import defaultdict, Counter, deque
from bisect import bisect, bisect_left
import math
from itertools import permutations
import queue


def sumOfDigits(x):
    prod = 1
    while x:
        prod *= x % 10
        x //= 10
    return prod


def findMax(x):
    b = 1
    ans = x
    while x != 0:
        cur = (x - 1) * b + (b - 1)
        if sumOfDigits(cur) > sumOfDigits(ans) or (sumOfDigits(cur) == sumOfDigits(ans) and cur > ans):
            ans = cur
        x = x // 10
        b = b * 10
    return ans


I = stdin.readline
n = int(I())
ans = findMax(n)
prod = 1
for i in str(ans):
    prod *= int(i)
print(prod)
