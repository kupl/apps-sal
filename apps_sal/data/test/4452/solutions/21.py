from collections import deque, defaultdict
import random
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
for i in range(t):
    n = input().strip()
    k = len(n) - 1
    l = []
    for i in range(len(n)):
        if n[i] != '0':
            l.append(int(n[i]) * pow(10, k))
        k -= 1
    print(len(l))
    print(*l)
