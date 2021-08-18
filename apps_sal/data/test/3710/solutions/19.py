import collections as col
import math
import sys
import math
input = sys.stdin.readline


def getInts():
    return [int(s) for s in input().split()]


def getInt():
    return int(input())


def getStrs():
    return [s for s in input().split()]


def getStr():
    return input().strip()


def listStr():
    return list(input().strip())


def solve():
    N, K = getInts()
    C = getInts()
    lcm = 1
    for c in C:
        lcm = lcm * c // math.gcd(lcm, c)
        lcm = math.gcd(lcm, K)
    return "Yes" if lcm == K else "No"


print(solve())
