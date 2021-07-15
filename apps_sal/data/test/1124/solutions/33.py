import sys
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()
from math import gcd
from functools import reduce
def resolve():
    input()
    print(reduce(gcd, map(int, input().split())))
resolve()
