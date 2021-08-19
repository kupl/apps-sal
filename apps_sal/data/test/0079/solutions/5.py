"""
    Author : thekushalghosh
    Team   : CodeDiggers
"""
import sys
import math
input = sys.stdin.readline


def inp():
    return int(input())


def inlt():
    return list(map(int, input().split()))


def insr():
    s = input()
    return s[:len(s) - 1]


def invr():
    return map(int, input().split())


t = 1
for tt in range(t):
    m = int(input())
    q = [0] * (m + 1)
    c = 1
    for i in range(m, 1, -1):
        w = m // i * pow(m, 1000000007 - 2, 1000000007)
        q[i] = w * pow(1 - w, 1000000007 - 2, 1000000007) % 1000000007
        for j in range(2 * i, m + 1, i):
            q[i] = (q[i] - q[j]) % 1000000007
        c = c + q[i]
    print(c % 1000000007)
