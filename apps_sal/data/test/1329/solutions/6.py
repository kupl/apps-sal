import sys
import heapq as hq
import itertools
import math
import collections


def ma():
    return map(int, input().split())


def lma():
    return list(map(int, input().split()))


def tma():
    return tuple(map(int, input().split()))


def ni():
    return int(input())


def yn(fl):
    return print('YES') if fl else print('NO')


n = ni()


def factorize(n):
    b = 2
    fct = [(1, 1)]
    while b * b <= n:
        cnt = 0
        while n % b == 0:
            n //= b
            cnt += 1
        if cnt >= 1:
            fct.append((b, cnt))
        b = b + 1
    if n > 1:
        fct.append((n, 1))
    return fct


co = collections.Counter()
for i in range(2, n + 1):
    fct = factorize(i)
    for (num, cnt) in fct:
        if num > 1:
            co[num] += cnt
f4 = 0
f2 = 0
f14 = 0
f24 = 0
f74 = 0
for cnt in co.values():
    if cnt >= 74:
        f74 += 1
    if cnt >= 24:
        f24 += 1
    if cnt >= 14:
        f14 += 1
    if cnt >= 4:
        f4 += 1
    if cnt >= 2:
        f2 += 1
ans = f74 + f24 * (f2 - 1) + f14 * (f4 - 1) + f4 * (f4 - 1) // 2 * (f2 - 2)
print(ans)
