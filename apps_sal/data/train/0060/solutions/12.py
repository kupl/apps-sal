"""
    Author: Sagar Pandey

"""
import sys
import os
from math import sqrt, log, log2, log10, gcd, floor, pow, sin, cos, tan, pi, inf, factorial
from copy import copy, deepcopy
from sys import stdin, stdout
from collections import Counter, defaultdict, deque
from itertools import permutations
import heapq
from bisect import bisect_left as bl
from bisect import bisect_right as br
from bisect import bisect
mod = 1000000007


def iinp():
    return int(sys.stdin.readline())


def inp():
    return sys.stdin.readline().strip()


def strl():
    return list(inp().strip().split(' '))


def intl():
    return list(map(int, inp().split(' ')))


def mint():
    return list(map(int, inp().split()))


def flol():
    return list(map(float, inp().split(' ')))


def flush():
    return stdout.flush()


def permute(nums):

    def fun(arr, nums, cur, v):
        if len(cur) == len(nums):
            arr.append(cur.copy())
        i = 0
        while i < len(nums):
            if v[i]:
                i += 1
                continue
            else:
                cur.append(nums[i])
                v[i] = 1
                fun(arr, nums, cur, v)
                cur.pop()
                v[i] = 0
                i += 1
        return arr
    res = []
    nums.sort()
    v = [0] * len(nums)
    return fun(res, nums, [], v)


def subsets(res, index, arr, cur):
    res.append(cur.copy())
    for i in range(index, len(arr)):
        cur.append(arr[i])
        subsets(res, i + 1, arr, cur)
        cur.pop()
    return res


def sieve(N):
    root = int(sqrt(N))
    primes = [1] * (N + 1)
    (primes[0], primes[1]) = (0, 0)
    for i in range(2, root + 1):
        if primes[i]:
            for j in range(i * i, N + 1, i):
                primes[j] = 0
    return primes


def bs(arr, l, r, x):
    if x < arr[0] or x > arr[len(arr) - 1]:
        return -1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1


def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    p = int(sqrt(n))
    for i in range(5, p + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def solve():
    (a, b) = mint()
    print(a ^ b)


for _ in range(iinp()):
    solve()
