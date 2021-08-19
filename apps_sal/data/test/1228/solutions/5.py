from collections import deque, defaultdict
import math as mt
import sys
import string
import bisect
input = sys.stdin.readline


def L():
    return list(map(int, input().split()))


def Ls():
    return list(input().split())


def M():
    return list(map(int, input().split()))


def I():
    return int(input())


n = I()
if n % 4 == 0:
    print(1, 'A')
if n % 4 == 1:
    print(0, 'A')
if n % 4 == 2:
    print(1, 'B')
if n % 4 == 3:
    print(2, 'A')
