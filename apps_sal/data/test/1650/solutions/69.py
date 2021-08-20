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
    return print('Yes') if fl else print('No')


mod = 10 ** 9 + 7
L = input()
n = len(L)
dp1 = [0] * n
dp2 = [0] * n
dp1[0] = 1
dp2[0] = 2
for i in range(1, n):
    if L[i] == '1':
        dp1[i] = (2 + 1) * dp1[i - 1] + 1 * dp2[i - 1]
        dp2[i] = 2 * dp2[i - 1]
    elif L[i] == '0':
        dp1[i] = (2 + 1) * dp1[i - 1]
        dp2[i] = dp2[i - 1]
    dp1[i] %= mod
    dp2[i] %= mod
print((dp1[n - 1] + dp2[n - 1]) % mod)
