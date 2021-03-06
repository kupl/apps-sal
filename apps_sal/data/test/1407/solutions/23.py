from collections import deque, defaultdict
import math
import sys
import string
import bisect
input = sys.stdin.readline


def L():
    return list(map(int, input().split()))


def Ls():
    return list(input().split())


def M():
    return list(map(int, input().split()))


def I():
    return int(input())


def find_ge(a, x):
    """Find leftmost item greater than or equal to x"""
    i = bisect.bisect_left(a, x)
    if i != len(a):
        return a[i]
    raise ValueError


MAX_SIZE = 1000005
isprime = [True] * MAX_SIZE
prime = []
SPF = [None] * MAX_SIZE


def manipulated_seive(N):
    isprime[0] = isprime[1] = False
    for i in range(2, N):
        if isprime[i] == True:
            prime.append(i)
            SPF[i] = i
        j = 0
        while j < len(prime) and i * prime[j] < N and (prime[j] <= SPF[i]):
            isprime[i * prime[j]] = False
            SPF[i * prime[j]] = prime[j]
            j += 1


manipulated_seive(MAX_SIZE)
(n, m) = M()
g = []
f = [0] * m
mi = MAX_SIZE
for i in range(n):
    l = L()
    for k in range(m):
        l[k] = find_ge(prime, l[k]) - l[k]
        f[k] += l[k]
    g.append(l)
    r = sum(l)
    if r < mi:
        mi = r
print(min(min(f), mi))
