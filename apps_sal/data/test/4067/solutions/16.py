import math
import bisect
import itertools
import sys


def I():
    return sys.stdin.readline()


mod = 10 ** 9 + 7
'fact=[1]*100001\nifact=[1]*100001\nfor i in range(1,100001):\n    fact[i]=((fact[i-1])*i)%mod\n    ifact[i]=((ifact[i-1])*pow(i,mod-2,mod))%mod\ndef ncr(n,r):\n    return (((fact[n]*ifact[n-r])%mod)*ifact[r])%mod\ndef npr(n,r):\n    return (((fact[n]*ifact[n-r])%mod))\n    '


def mindiff(a):
    b = a[:]
    b.sort()
    m = 10000000000
    for i in range(len(b) - 1):
        if b[i + 1] - b[i] < m:
            m = b[i + 1] - b[i]
    return m


def lcm(a, b):
    return a * b // math.gcd(a, b)


def merge(a, b):
    i = 0
    j = 0
    c = 0
    ans = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            ans.append(a[i])
            i += 1
        else:
            ans.append(b[j])
            c += len(a) - i
            j += 1
    ans += a[i:]
    ans += b[j:]
    return (ans, c)


def mergesort(a):
    if len(a) == 1:
        return (a, 0)
    mid = len(a) // 2
    (left, left_inversion) = mergesort(a[:mid])
    (right, right_inversion) = mergesort(a[mid:])
    (m, c) = merge(left, right)
    c += left_inversion + right_inversion
    return (m, c)


def is_prime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    if num == 3:
        return True
    if num % 2 == 0:
        return False
    if num % 3 == 0:
        return False
    t = 5
    a = 2
    while t <= int(math.sqrt(num)):
        if num % t == 0:
            return False
        t += a
        a = 6 - a
    return True


def ceil(a, b):
    if a % b == 0:
        return a // b
    else:
        return a // b + 1


def binsearch(arr, b, low, high):
    if low == high:
        return low
    if arr[math.ceil((low + high) / 2)] < b:
        return binsearch(arr, b, low, math.ceil((low + high) / 2) - 1)
    else:
        return binsearch(arr, b, math.ceil((low + high) / 2), high)


def ncr1(n, r):
    s = 1
    for i in range(min(n - r, r)):
        s *= n - i
        s %= mod
        s *= pow(i + 1, mod - 2, mod)
        s %= mod
    return s


def calc(n, m, r):
    s = 0
    for i in range(0, r + 1, 2):
        s += ncr1(n, i) * ncr1(m, i)
        s %= mod
    return s


n = int(input())
s = input()
c = ''
d = {'0': 0, '1': 0, '2': 0}
ans = n // 3
for i in s:
    d[i] += 1
d1 = {'0': 0, '1': 0, '2': 0}
for i in s:
    if d['0'] < ans:
        k = '0'
    elif d['1'] < ans:
        k = '1'
    elif d['2'] < ans:
        k = '2'
    if d[i] > ans:
        if int(i) < int(k) and d1[i] == ans or int(i) > int(k):
            c += k
            d[i] -= 1
            d[k] += 1
            d1[k] += 1
        else:
            c += i
            d1[i] += 1
    else:
        c += i
        d1[i] += 1
print(c)
