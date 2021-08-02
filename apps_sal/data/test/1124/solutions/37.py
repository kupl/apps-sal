import sys
import math
import collections
import itertools
import functools
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N = int(input())
a = list(map(int, input().split()))

ans = functools.reduce(math.gcd, a)
print(ans)
