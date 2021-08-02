# -*- coding: utf-8 -*-

#############
# Libraries #
#############

from functools import lru_cache
from collections import Counter
from collections import deque
from collections import defaultdict
import heapq
import bisect
import math
import sys
input = sys.stdin.readline

#from math import gcd

#############
# Constants #
#############

MOD = 10**9 + 7
INF = float('inf')
AZ = "abcdefghijklmnopqrstuvwxyz"

#############
# Functions #
#############

######INPUT######


def I(): return int(input().strip())
def S(): return input().strip()
def IL(): return list(map(int, input().split()))
def SL(): return list(map(str, input().split()))
def ILs(n): return list(int(input()) for _ in range(n))
def SLs(n): return list(input().strip() for _ in range(n))
def ILL(n): return [list(map(int, input().split())) for _ in range(n)]
def SLL(n): return [list(map(str, input().split())) for _ in range(n)]

######OUTPUT######


def P(arg): print(arg); return
def Y(): print("Yes"); return
def N(): print("No"); return
def E(): return()
def PE(arg): print(arg); return()
def YE(): print("Yes"); return()
def NE(): print("No"); return()

#####Shorten#####


def DD(arg): return defaultdict(arg)

#####Inverse#####


def inv(n): return pow(n, MOD - 2, MOD)


######Combination######
kaijo_memo = []


def kaijo(n):
    if(len(kaijo_memo) > n):
        return kaijo_memo[n]
    if(len(kaijo_memo) == 0):
        kaijo_memo.append(1)
    while(len(kaijo_memo) <= n):
        kaijo_memo.append(kaijo_memo[-1] * len(kaijo_memo) % MOD)
    return kaijo_memo[n]


gyaku_kaijo_memo = []


def gyaku_kaijo(n):
    if(len(gyaku_kaijo_memo) > n):
        return gyaku_kaijo_memo[n]
    if(len(gyaku_kaijo_memo) == 0):
        gyaku_kaijo_memo.append(1)
    while(len(gyaku_kaijo_memo) <= n):
        gyaku_kaijo_memo.append(gyaku_kaijo_memo[-1] * pow(len(gyaku_kaijo_memo), MOD - 2, MOD) % MOD)
    return gyaku_kaijo_memo[n]


def nCr(n, r):
    if n == r:
        return 1
    if n < r or r < 0:
        return 0
    ret = 1
    ret = ret * kaijo(n) % MOD
    ret = ret * gyaku_kaijo(r) % MOD
    ret = ret * gyaku_kaijo(n - r) % MOD
    return ret

######Factorization######


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5 // 1)) + 1):
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

#####MakeDivisors######


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors

#####MakePrimes######


def make_primes(N):
    max = int(math.sqrt(N))
    seachList = [i for i in range(2, N + 1)]
    primeNum = []
    while seachList[0] <= max:
        primeNum.append(seachList[0])
        tmp = seachList[0]
        seachList = [i for i in seachList if i % tmp != 0]
    primeNum.extend(seachList)
    return primeNum

#####GCD#####


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

#####LCM#####


def lcm(a, b):
    return a * b // gcd(a, b)

#####BitCount#####


def count_bit(n):
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count

#####ChangeBase#####


def base_10_to_n(X, n):
    if X // n:
        return base_10_to_n(X // n, n) + [X % n]
    return [X % n]


def base_n_to_10(X, n):
    return sum(int(str(X)[-i - 1]) * n**i for i in range(len(str(X))))


def base_10_to_n_without_0(X, n):
    X -= 1
    if X // n:
        return base_10_to_n_without_0(X // n, n) + [X % n]
    return [X % n]

#####IntLog#####


def int_log(n, a):
    count = 0
    while n >= a:
        n //= a
        count += 1
    return count

#############
# Main Code #
#############


A, B = IL()
print(100, 100)
A = ["#"] * (25 * 50 - (A - 1)) + ["."] * (A - 1)
B = ["#"] * (B - 1) + ["."] * (25 * 50 - (B - 1))
for j in range(25):
    for i in range(50):
        print(A.pop(), end="")
        if i == 49:
            print("#")
        else:
            print("#", end="")
    print("#" * 100)
for j in range(25):
    print("." * 100)
    for i in range(50):
        print(B.pop(), end="")
        if i == 49:
            print(".")
        else:
            print(".", end="")
