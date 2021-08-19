import time
import math as mt
import bisect as bs
import sys
from sys import stdin, stdout
from collections import deque
from fractions import Fraction
from collections import Counter
from collections import OrderedDict
pi = 3.141592653589793


def II():
    return int(stdin.readline())


def IP():
    return list(map(int, stdin.readline().split()))


def L():
    return list(map(int, stdin.readline().split()))


def P(x):
    return stdout.write(str(x) + '\n')


def PI(x, y):
    return stdout.write(str(x) + ' ' + str(y) + '\n')


def lcm(a, b):
    return a * b // gcd(a, b)


def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    if a > b:
        return gcd(a % b, b)
    else:
        return gcd(a, b % a)


def bfs(adj, v):
    visited = [False] * (v + 1)
    q = deque()
    while q:
        pass


def sieve():
    li = [True] * (2 * 10 ** 5 + 5)
    (li[0], li[1]) = (False, False)
    for i in range(2, len(li), 1):
        if li[i] == True:
            for j in range(i * i, len(li), i):
                li[j] = False
    prime = []
    for i in range(2 * 10 ** 5 + 5):
        if li[i] == True:
            prime.append(i)
    return prime


def setBit(n):
    count = 0
    while n != 0:
        n = n & n - 1
        count += 1
    return count


mx = 10 ** 7
spf = [mx] * (mx + 1)


def SPF():
    spf[1] = 1
    for i in range(2, mx + 1):
        if spf[i] == mx:
            spf[i] = i
            for j in range(i * i, mx + 1, i):
                if i < spf[j]:
                    spf[j] = i
    return


def readTree(n, e):
    adj = [set() for i in range(n + 1)]
    for i in range(e):
        (u1, u2) = IP()
        adj[u1].add(u2)
    return adj


mod = 10 ** 9 + 7


def solve():
    a = II()
    s = input()
    li = [int(i) for i in s]
    n = len(li)
    pref = [li[0]] + [0] * (n - 1)
    for i in range(1, n):
        pref[i] = pref[i - 1] + li[i]
    pref.insert(0, 0)
    d = {}
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            val = pref[j] - pref[i - 1]
            d[val] = d.get(val, 0) + 1
    ans = 0
    if a != 0:
        for ele in d:
            if ele != 0:
                if a % ele == 0 and a // ele in d:
                    ans += d[ele] * d[a // ele]
    else:
        cnt = d.get(0, 0)
        ans = 2 * cnt * (n * (n + 1) // 2) - cnt ** 2
    P(ans)
    return


t = 1
for i in range(t):
    solve()
