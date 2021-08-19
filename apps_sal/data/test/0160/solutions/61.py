import sys
import math
import heapq
sys.setrecursionlimit(10 ** 7)
INTMAX = 9223372036854775807
INTMIN = -9223372036854775808
DVSR = 1000000007


def POW(x, y):
    return pow(x, y, DVSR)


def INV(x, m=DVSR):
    return pow(x, m - 2, m)


def DIV(x, y, m=DVSR):
    return x * INV(y, m) % m


def LI():
    return [int(x) for x in input().split()]


def LF():
    return [float(x) for x in input().split()]


def LS():
    return input().split()


def II():
    return int(input())


def FLIST(n):
    res = [1]
    for i in range(1, n + 1):
        res.append(res[i - 1] * i % DVSR)
    return res


def gcd(x, y):
    if x < y:
        (x, y) = (y, x)
    div = x % y
    while div != 0:
        (x, y) = (y, div)
        div = x % y
    return y


(N, K) = LI()
AS = LI()
SUMM = sum(AS)
DIVS = set()
for i in range(1, 40000):
    if SUMM % i == 0:
        DIVS.add(i)
        DIVS.add(SUMM // i)
DIFF = [0] * N
res = 0
for div in DIVS:
    for i in range(N):
        DIFF[i] = AS[i] % div
    DIFF.sort()
    i = 0
    j = N - 1
    sm = 0
    cost = 0
    while i <= j:
        if sm + DIFF[j] >= div:
            sm -= div - DIFF[j]
            j -= 1
        else:
            cost += DIFF[i]
            sm += DIFF[i]
            i += 1
    if cost <= K:
        res = max(res, div)
print(res)
