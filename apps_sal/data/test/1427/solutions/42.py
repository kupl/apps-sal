import sys
import math
import collections
import itertools
input = sys.stdin.readline
m = 10**9 + 7
"""nを素因数分解"""
"""2以上の整数n => [[素因数, 指数], ...]の2次元リスト"""


def factorization(n):
    arr = []
    temp = n
    i = 2
    if temp % i == 0:
        cnt = 0
        while temp % i == 0:
            cnt += 1
            temp //= i
        arr.append([i, cnt])

    for i in range(3, int(-(-n**0.5 // 1)) + 1, 2):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


N = int(input())
A = list(map(int, input().split()))
d = collections.defaultdict(int)
for a in A:
    arr = factorization(a)
    for ar in arr:
        if d[ar[0]] < ar[1]:
            d[ar[0]] = ar[1]

gcd = 1
for key, val in list(d.items()):
    gcd = gcd * pow(key, val)

ans = 0
for a in A:
    ans = ans + gcd // a
print((ans % m))
