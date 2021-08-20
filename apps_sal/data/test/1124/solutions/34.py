from sys import stdin, stdout
from collections import *
from math import ceil, floor, log, gcd


def st():
    return list(stdin.readline().strip())


def li():
    return list(map(int, stdin.readline().split()))


def mp():
    return list(map(int, stdin.readline().split()))


def inp():
    return int(stdin.readline())


def pr(n):
    return stdout.write(str(n) + '\n')


mod = 1000000007
INF = float('inf')


def solve():
    n = inp()
    l = li()
    g = l[0]
    for i in range(1, n):
        g = gcd(g, l[i])
    pr(g)


for _ in range(1):
    solve()
