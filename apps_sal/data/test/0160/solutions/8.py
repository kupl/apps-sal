import sys
import math
import heapq
sys.setrecursionlimit(10**7)
INTMAX = 9223372036854775807
INTMIN = -9223372036854775808
DVSR = 1000000007
def POW(x, y): return pow(x, y, DVSR)
def INV(x, m=DVSR): return pow(x, m - 2, m)
def DIV(x, y, m=DVSR): return (x * INV(y, m)) % m
def LI(): return [int(x) for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()
def II(): return int(input())


def FLIST(n):
    res = [1]
    for i in range(1, n + 1):
        res.append(res[i - 1] * i % DVSR)
    return res


def gcd(x, y):
    if x < y:
        x, y = y, x
    div = x % y
    while div != 0:
        x, y = y, div
        div = x % y
    return y


N, K = LI()
AS = LI()
SUMM = sum(AS)

DIVS = set()
for i in range(1, 40000):
    if SUMM % i == 0:
        DIVS.add(i)
        DIVS.add(SUMM // i)
# DIVS.sort(reversed=True)
# print(DIVS)

DIFF = [0] * N
ACC = [0] * N

# res = 0

for div in sorted(DIVS, reverse=True):
    for i in range(N):
        DIFF[i] = AS[i] % div
    DIFF.sort()
    ACC[0] = DIFF[0]
    for i in range(1, N):
        ACC[i] = ACC[i - 1] + DIFF[i]
    # print(ACC)
    for i in range(N - 1):
        left = ACC[i]
        right = (N - 1 - i) * div - (ACC[N - 1] - ACC[i])
        if left % div == right % div:
            if max(left, right) <= K:
                # print(max(left, right))
                print(div)
                return


# print(DIFF)
# print(res)
