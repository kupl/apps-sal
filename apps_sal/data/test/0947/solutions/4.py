from collections import defaultdict
import math as mt
import sys
import string
input = sys.stdin.readline


def L():
    return list(map(int, input().split()))


def Ls():
    return list(input().split())


def M():
    return list(map(int, input().split()))


def I():
    return int(input())


t = I()
for _ in range(t):
    n = I()
    f = 0
    for i in range(2, int(mt.sqrt(n)) + 1):
        if n % i == 0:
            f = 1
            key = i
            break
    if f:
        print(n // key, n - n // key)
    else:
        print(1, n - 1)
