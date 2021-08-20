from collections import deque, defaultdict
import sys
import math
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


n = int(input())
for _ in range(n):
    k = I()
    g = []
    l = [0] + L()
    for i in range(1, k + 1):
        s = i
        c = 1
        while l[s] != i:
            s = l[s]
            c += 1
        g.append(c)
    print(*g)
