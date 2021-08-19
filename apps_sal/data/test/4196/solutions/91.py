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


gcd = math.gcd
n = ni()
A = lma()
gcd_l = [1] * n
gcd_l[0] = A[0]
gcd_r = [1] * n
gcd_r[-1] = A[-1]
for i in range(1, n):
    gcd_l[i] = gcd(A[i], gcd_l[i - 1])
    gcd_r[-i - 1] = gcd(A[-i - 1], gcd_r[-i])
ans = max(gcd_l[-2], gcd_r[1])
for i in range(1, n - 1):
    ggg = gcd(gcd_l[i - 1], gcd_r[i + 1])
    ans = max(ans, ggg)
print(ans)
