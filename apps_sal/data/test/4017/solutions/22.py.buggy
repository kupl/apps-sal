import math
import bisect
import itertools
import sys
mod = 10**9 + 7
'''fact=[1]*1001
ifact=[1]*1001
for i in range(1,1001):
    fact[i]=((fact[i-1])*i)%mod
    ifact[i]=((ifact[i-1])*pow(i,mod-2,mod))%mod
def ncr(n,r):
    return (((fact[n]*ifact[n-r])%mod)*ifact[r])%mod
def npr(n,r):
    return (((fact[n]*ifact[n-r])%mod))
    '''


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
    return ans, c


def mergesort(a):
    if len(a) == 1:
        return a, 0
    mid = len(a) // 2
    left, left_inversion = mergesort(a[:mid])
    right, right_inversion = mergesort(a[mid:])
    m, c = merge(left, right)
    c += (left_inversion + right_inversion)
    return m, c


def is_prime(num):
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
        return (a // b + 1)


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
        s *= (n - i)
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


# /////////////////////////////////////////////////////////////////////////////////////////////////
n = int(input())

a = list(map(int, input().split()))
s = sum(a)
b = []
count = 0
c = []
for i in range(n):
    b.append(s - a[i])
ma = min(a)
sm = min(a)
for i in range(n):
    if ma < a[i]:
        sm = ma
        ma = a[i]
    elif sm < a[i]:
        sm = a[i]
for i in range(n):
    if a[i] == ma:
        if b[i] / 2 == sm:
            count += 1
            c.append(i + 1)
    else:
        # print(b[i])
        if b[i] / 2 == ma:
            count += 1
            c.append(i + 1)
# print(b)
# print(ma,sm)
if count == 0:
    print(count)
    return
print(count)
print(*c)
