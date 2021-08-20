"""
arr = list(map(int, input().split()))
n,k=map(int, input().split())
"""
import math
import sys


def inp():
    return int(input())


def inlt():
    return list(map(int, input().split()))


def insr():
    s = input()
    return list(s[:len(s) - 1])


def invr():
    return list(map(int, input().split()))


test_cases = int(input())
for _ in range(test_cases):
    sides = int(input())
    sides *= 2
    apothem = 1 / (2 * math.tan(180 / sides * (math.pi / 180)))
    print(2 * apothem)
