from bisect import bisect_left
n, m = map(int, input().split())
import math
import numpy as np
import decimal
import collections
import itertools
import sys
def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]
def unite(x, y):
    p = find(x)
    q = find(y)
    if p == q:
        return None
    if p > q:
        p,q = q,p
    par[p] += par[q]
    par[q] = p
def same(x, y):
    return find(x) == find(y)
def size(x):
    return -par[find(x)]
par = [-1 for i in range(n)]
def prime_numbers(x):
    if x < 2:
        return []
    prime_numbers = [i for i in range(x)]
    prime_numbers[1] = 0
    for prime_number in prime_numbers:
        if prime_number > math.sqrt(x):
            break
        if prime_number == 0:
            continue
        for composite_number in range(2 * prime_number, x, prime_number):
            prime_numbers[composite_number] = 0
    return [prime_number for prime_number in prime_numbers if prime_number != 0]
def is_prime(x):
    if x < 2:
        return False
    if x == 2 or x == 3 or x == 5:
        return True
    if x % 2 == 0 or x % 3 == 0 or x % 5 == 0:
        return False
    prime_number = 7
    difference = 4
    while prime_number <= math.sqrt(x):
        if x % prime_number == 0:
            return False
        prime_number += difference
        difference = 6 - difference
    return True
BIT = [0] * (n + 1)
def add(i, x):
    while i <= n:
        BIT[i] += x
        i += i & -i
def query(i):
    s = 0
    while i > 0:
        s += BIT[i]
        i -= i & -i
    return s
a = list(map(int, input().split()))
a.sort(reverse=True)
l, r = 0, 10 ** 6
while r - l > 1:
    m2 = (l + r) // 2
    cnt = 0
    ind = n - 1
    for i in a:
        while ind >= 0 and a[ind] + i < m2:
            ind -= 1
        cnt += ind + 1
    if cnt >= m:
        l = m2
    else:
        r = m2
cum = [0]
for i in a:
    cum.append(cum[-1] + i)
ans = 0
cnt2 = 0
ind2 = n - 1
b = l
for i in a:
    while ind2 >= 0 and a[ind2] + i < b:
        ind2 -= 1
    cnt2 += ind2 + 1
    ans += (ind2 + 1) * i + cum[ind2 + 1]
print(ans - (cnt2 - m) * b)
