from functools import reduce
from math import gcd
import sys
INF = 1 << 60
MOD = 10 ** 9 + 7
sys.setrecursionlimit(2147483647)


def input():
    return sys.stdin.readline().rstrip()


def resolve():
    input()
    print(reduce(gcd, map(int, input().split())))


resolve()
